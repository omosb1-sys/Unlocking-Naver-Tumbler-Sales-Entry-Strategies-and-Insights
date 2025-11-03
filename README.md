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

## 인사이트
텀블러판매마켓에서 3-5만원대의 제품은 경쟁이 가장 치열한 시장임을 "price_distribution.png'파일에 나타난다. 
용량별가격 산점도 그래프와 함께 추론해보면 " 2만원"대 텀블러가 가장 경쟁이 낮은 가격대이다. 
물론 더 낮은 가격대와 경쟁이 낮은 시장은 저가시장이다.
하지만 손익분기점을 생각한다면 새롭게 진입하는 판매자라면 특히 네이버쇼핑에서는 " 2만원대"가 경쟁도, 손익분기점 을 생각한다면 가장 적합한 진입가격대라는 결론이 나온다. 
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
