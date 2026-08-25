import pandas as pd
import numpy as np
import glob
import os
import re
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.pipeline import Pipeline

# 1. 데이터 로드 (유연한 경로 처리)
base_path = Path(__file__).parent if "__file__" in locals() else Path(".")
candidate_dirs = [
    base_path / "data",
    base_path / "naver_shopping_analysis" / "data",
    Path("./data"),
    Path("./naver_shopping_analysis/data")
]

data_dir = next((d for d in candidate_dirs if d.exists() and list(d.glob("*.csv"))), None)

if data_dir is None:
    raise FileNotFoundError("CSV 데이터 디렉토리를 찾을 수 없습니다. data/ 디렉토리에 naver_shopping_*.csv 파일을 배치해주세요.")

csv_files = list(data_dir.glob("*.csv"))
df = pd.concat([pd.read_csv(f, encoding='utf-8-sig') for f in csv_files], ignore_index=True)

# 전처리
df = df.drop_duplicates(subset=['product_id']).copy() if 'product_id' in df.columns else df.drop_duplicates().copy()
df['lprice'] = pd.to_numeric(df['lprice'], errors='coerce')
df = df.dropna(subset=['lprice', 'title'])

# 이상치 제거 (하위 1%, 상위 1% 제거로 모델 안정성 확보)
lower = df['lprice'].quantile(0.01)
upper = df['lprice'].quantile(0.99)
df_clean = df[(df['lprice'] >= lower) & (df['lprice'] <= upper)].copy()

print(f"🧹 데이터 정제 후: {len(df_clean)}개 샘플")

# 2. 텍스트 정제 함수
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^가-힣a-z0-9\s]', ' ', text)
    return text

df_clean['clean_title'] = df_clean['title'].apply(clean_text)

# 3. 데이터 분할 (Data Leakage 방지: Fit 전에 Train/Test 먼저 분리)
y = np.log1p(df_clean['lprice'])
X_train_raw, X_test_raw, y_train, y_test = train_test_split(
    df_clean['clean_title'], y, test_size=0.2, random_state=42
)

# 4. Pipeline 구성 (TF-IDF Vectorizer + Ridge Regression)
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=3000, ngram_range=(1, 2), min_df=3)),
    ('ridge', Ridge(alpha=1.0))
])

# Train 데이터에만 fit_transform 수행
pipeline.fit(X_train_raw, y_train)

# 5. 평가 (Test 데이터에는 transform만 적용되어 평가됨)
y_pred_log = pipeline.predict(X_test_raw)
y_pred = np.expm1(y_pred_log)
y_real = np.expm1(y_test)

mae = mean_absolute_error(y_real, y_pred)
r2 = r2_score(y_real, y_pred)

print(f"\n🚀 모델 성능 평가 (Leakage 제거 후)")
print(f"평균 오차(MAE): 약 {mae:,.0f}원")
print(f"설명력(R2 Score): {r2:.3f}")

# 6. 해석: 키워드별 가격 기여도 (회귀 계수 산출)
vectorizer = pipeline.named_steps['tfidf']
model = pipeline.named_steps['ridge']
feature_names = vectorizer.get_feature_names_out()
coefs = model.coef_

coef_df = pd.DataFrame({'keyword': feature_names, 'coefficient': coefs})
coef_df['abs_coef'] = coef_df['coefficient'].abs()
coef_df = coef_df.sort_values(by='coefficient', ascending=False)

print("\n💎 [Premium Keywords] 가격을 상승시키는 단어 TOP 15")
print(coef_df.head(15)[['keyword', 'coefficient']])

print("\n📉 [Budget Keywords] 가격을 하락시키는 단어 TOP 15")
print(coef_df.tail(15)[['keyword', 'coefficient']].sort_values(by='coefficient'))

# 7. 가격 예측 시뮬레이션 함수
def predict_price(title):
    clean = clean_text(title)
    pred_log = pipeline.predict([clean])[0]
    return np.expm1(pred_log)

print("\n🧪 [오프라인 가격 예측 시뮬레이션]")
test_titles = [
    "스타벅스 대용량 텀블러",
    "스탠리 퀜처 한정판",
    "다이소 가성비 물병"
]

for t in test_titles:
    price = predict_price(t)
    print(f"상품명: '{t}' --> 시뮬레이션 예측 가격: {price:,.0f}원")

# 8. 결과 저장 (시각화용)
coef_df.head(20).to_csv(base_path / 'top_positive_keywords.csv', index=False)
coef_df.tail(20).to_csv(base_path / 'top_negative_keywords.csv', index=False)
