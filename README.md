# 네이버 쇼핑 텀블러 데이터 분석 프로젝트

이 프로젝트는 네이버 쇼핑에서 텀블러 제품 데이터를 수집하고 분석한 내용입니다. 가격 분포, 용량-가격 관계 등을 Jupyter Notebook으로 시각화했습니다.

## 주요 파일
- `텀블러분석(네이버쇼핑).ipynb`: 메인 분석 노트북 (데이터 처리, 그래프 생성)
- `tumbler_analyzed.csv`: 분석된 CSV 데이터
- `price_distribution.png`: 가격 분포 그래프
- `capacity_price.png`: 용량 vs 가격 산점도 그래프

## 사용 방법
1. Jupyter Notebook 설치: `pip install notebook`
2. 노트북 실행: `jupyter notebook 텀블러분석(네이버쇼핑).ipynb`
3. 데이터는 네이버 쇼핑 API 또는 크롤링으로 수집 (코드 내 참조)

## 분석 결과 요약
- 평균 가격: 약 20,000원
- 인기 용량: 500ml
- 상관 관계: 용량이 클수록 가격 상승

---

## Add English README (English Version)

# Naver Shopping Tumbler Data Analysis Project

This project analyzes tumbler product data from Naver Shopping. It includes price distribution and capacity-price relationships visualized in Jupyter Notebook.

## Key Files
- `tumbler_analysis(naver_shopping).ipynb`: Main analysis notebook (data processing, graphs)
- `tumbler_analyzed.csv`: Analyzed CSV data
- `price_distribution.png`: Price distribution graph
- `capacity_price.png`: Capacity vs Price scatter plot

## How to Use
1. Install Jupyter Notebook: `pip install notebook`
2. Run the notebook: `jupyter notebook tumbler_analysis(naver_shopping).ipynb`
3. Data collected via Naver Shopping API or crawling (refer to code)

## Analysis Summary
- Average price: about 20,000 KRW
- Popular capacity: 500ml
- Correlation: Higher capacity leads to higher price

For more details, check the notebook!