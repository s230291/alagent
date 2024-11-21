# 분류 모델 웹앱 만들기

import streamlit as st

# 1. 기계학습 모델 파일 로드
import joblib
model = joblib.load('linear_regression_model.pkl')

# 2. 모델 설명 
st.title('심리적 요인과 환경에 따른 학업성취도 예측 에이전트')
st.subheader('모델 설명 ')
st.write(' - 기계학습 알고리즘 : 선형 회귀 ')
st.write(' - 학습 데이터 출처 : https://www.kaggle.com/')
st.write(' - 훈련    데이터 : 246건')
st.write(' - 테스트 데이터 : 106건')
st.write(' - 모델 정확도 : -0.01') 
st.write(' - 독립변수 개수 : 5건')

# 3. 데이터시각화
col1, col2, col3 = st.columns( 3 )
with col1:
  st.subheader('데이터시각화1')
  st.image('시각화1.png')
with col2:
  st.subheader('데이터시각화2')
  st.image('시각화2.png')
with col3:
  st.subheader('데이터시각화3')
  st.image('시각화3.png')

# 4. 모델 활용
st.subheader('모델 활용')
st.write('***다음을 입력하세요. 인공지능이 당신의 학업성취도를 예측해드립니다.')

a = st.number_input(' 의욕지수 입력(1~4)', value=0)   # 사용자 입력
b = st.number_input(' 기분 입력(1~4)', value=0)
c = st.number_input(' 수면 입력(1~4)', value=0)
d = st.number_input(' 집중 입력(1~4)', value=0)
e = st.number_input(' 공부시간 입력 ', value=0)

if st.button('예측하기'):
  input_data[[a,b,c,d,e]]
  p = model.predict(input_data)
  if p[0] == 1 :
    st.success('')
  else:
    st.success('')
  











