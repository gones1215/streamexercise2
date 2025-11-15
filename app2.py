import streamlit as st

# 앱의 제목 설정
st.title('나의 첫 번째 스트림릿 앱')

# 간단한 텍스트 출력
st.write('환영합니다! 아래에 메시지를 입력해 보세요.')

# 사용자로부터 텍스트 입력 받기
user_input = st.text_input('여기에 메시지를 입력하세요:', '안녕하세요, 스트림릿!')

# 입력받은 텍스트를 다시 화면에 출력
st.write('사용자가 입력한 메시지:', user_input)
