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

a = st.selectbox(' 의욕지수 입력(1~4)', [1,2,3,4])   # 사용자 입력
b = st.selectbox(' 기분 입력(1~4)', [1,2,3,4])
c = st.selectbox(' 수면 입력(1~4)', [1,2,3,4])
d = st.selectbox(' 집중 입력(1~4)', [1,2,3,4])
e = st.selectbox(' 공부시간 입력( 1-2시간: 0, 2-4시간: 1, 4시간 이상: 2) ', [0,1,2])       #모르겠어요

if st.button('점수예측'):            # 사용자가 '점수예측' 버튼을 누르면
        input_data = [[a,b,c,d,e]]     # 사용자가 입력한 a,b,c 를 input_data에 저장하고
        p = model.predict(input_data)         # model이 예측한 값을 p에 저장한다
        round(p, 1)
        st.write(f"인공지능 예측점수는 {p}점 입니다.")
  











