import streamlit as st
import pandas as pd
import numpy as np

# 앱 제목 설정
st.title('나의 첫 스트림릿 앱')

# 텍스트 입력 받기
user_input = st.text_input("이름을 입력하세요:")

# 버튼 추가
if st.button('인사하기'):
    if user_input:
        st.write(f"안녕하세요, {user_input}님! 🥳")
    else:
        st.write("이름을 입력해주세요.")

# 슬라이더 추가 및 값 표시
x = st.slider('숫자를 선택하세요', 0, 100, 25)
st.write(f"선택한 숫자는 {x}입니다.")

# 데이터프레임 표시 예제
st.subheader('랜덤 데이터프레임')
dataframe = pd.DataFrame(
    np.random.randn(10, 3), # 10행 3열의 랜덤 데이터 생성
    columns=['a', 'b', 'c']
)
st.write(dataframe) # st.write() 함수로 텍스트, 데이터프레임 등 다양한 요소 표시 가능

# 라인 차트 그리기
st.subheader('랜덤 데이터 라인 차트')
st.line_chart(dataframe)
