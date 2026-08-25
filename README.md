# 🛍️ Naver Shopping Data Analysis: Pricing Strategy & Text Mining
> **Project Goal:** 네이버 쇼핑 '텀블러' 카테고리 데이터 분석을 통한 가격 결정 요인 발굴 및 키워드/이미지 기반 가격 전략 제안

![Status](https://img.shields.io/badge/Status-Completed-success)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![Sklearn](https://img.shields.io/badge/ML-Scikit--learn-F7931E?logo=scikit-learn&logoColor=white)

## 📊 Project Overview
본 프로젝트는 네이버 쇼핑 텀블러 카테고리 상품의 **상품명(Text) 및 썸네일(Image)** 특성이 **형성 가격(Price)**과 맺는 통계적 관계를 규명하고, 머신러닝 회귀 모델을 활용하여 가격 책정 및 상품명 최적화에 기여할 수 있는 데이터 기반 인사이트를 도출한 분석 프로젝트입니다.

---

## 🧪 Hypotheses & Exploratory Findings (가설 및 탐색적 분석)

1. **Text Feature Analysis (텍스트 특성)**:
   - 기능/스펙 중심 키워드(스텐, 진공 등) 대비 감성·브랜드 중심 키워드(에디션, 정품 등)가 고가격대 상품군에서 통계적으로 높은 빈도 및 양(+)의 회귀 계수를 보임.
2. **Keyword Position Analysis (키워드 배치 구조)**:
   - 주요 브랜드 키워드가 전면에 배치될 때 모델 예측가 및 평균 등록 가격이 상대적으로 높은 경향 확인 (평균 +4.3% 차이 관측).
3. **Visual Aesthetics (이미지 채도와 가격)**:
   - 썸네일 이미지의 채도(Saturation)와 상품 가격 간의 음(-)의 상관관계 관측 (원색 대비 차분한 톤의 프리미엄 포지셔닝 경향).

---

## 🛠️ Tech Stack & Methodology
* **Data Collection:** 네이버 쇼핑 크롤링 데이터 (2,110건 수집 및 전처리)
* **Text Mining & Feature Engineering:** TF-IDF Vectorizer (N-gram 1-2, Data Leakage 방지를 위해 Train-Test Split 후 학습)
* **Modeling:** Ridge Regression (L2 규제 기반 회귀 분석, 단어별 회귀 계수 산출)
* **Image Processing:** PIL & KMeans Clustering (HSV 채도/명도 통계량 추출)
* **Simulation:** 학습된 회귀 모델 기반 가상 시뮬레이션 (Counterfactual Title Simulation)

---

## 💡 Key Strategy & Simulation Insights

### 1. Title Keyword Optimization (상품명 최적화)
* 기능성 일반 명사보다는 브랜드 및 차별화 키워드를 전면에 배치하여 검색 노출 및 프리미엄 이미지 확보 권장.

### 2. Predictive Price Simulation (오프라인 가치 시뮬레이션)
* 학습된 Ridge 회귀 모델을 이용해 특정 제품(예: 마리슈타이거)의 상품명을 고가격대 군집 키워드로 변경 시, 모델 기준 예상 가격 변화율 약 **+86%** 시뮬레이션 결과 확인.
* *※ 본 시뮬레이션은 과거 데이터 기반의 오프라인 모델 추정치이며, 인과효과 검증을 위한 실제 온라인 A/B 테스트 진행을 권장합니다.*

### 3. Visual Positioning Strategy (썸네일 전략)
* 저가형 원색 썸네일 대비 낮은 채도의 톤앤매너가 프리미엄 포지셔닝에 긍정적인 통계적 연관성을 보임.

---

## 📈 Visualizations
| High-Value Keywords | Price Simulation (Lift) | Image Saturation |
| :---: | :---: | :---: |
| ![Keywords](./insights_premium_keywords.png) | ![Lift](./ab_test_lift.png) | ![Saturation](./image_saturation_price.png) |

---

## 📂 Deliverables & Project Structure
* [📄 분석 결과 보고서 (Report)](./Naver_Shopping_Optimization_Report_v2.md)
* [📝 상품명 변경 가이드라인 (Guideline)](./NAMING_GUIDELINE.md)
* [💻 가격 예측 모델 코드 (`price_predictor.py`)](./price_predictor.py)
* **[📓 전체 분석 노트북 (`Naver_Shopping_Pricing_Strategy.ipynb`)](./Naver_Shopping_Pricing_Strategy.ipynb)**

---
*Data Analysis & Engineering by Sebokoh*
