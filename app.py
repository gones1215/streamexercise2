import random
import streamlit as st

st.set_page_config(page_title="주기율표 퀴즈", page_icon="🔬")

st.title("🔬 주기율표 게임")
st.write("원자번호를 보고 **원소 기호**를 맞혀보세요! (최대 20문제)")

# 1~20번 원소 데이터
ELEMENTS_1_20 = [
    {"Z": 1,  "symbol": "H"},
    {"Z": 2,  "symbol": "He"},
    {"Z": 3,  "symbol": "Li"},
    {"Z": 4,  "symbol": "Be"},
    {"Z": 5,  "symbol": "B"},
    {"Z": 6,  "symbol": "C"},
    {"Z": 7,  "symbol": "N"},
    {"Z": 8,  "symbol": "O"},
    {"Z": 9,  "symbol": "F"},
    {"Z": 10, "symbol": "Ne"},
    {"Z": 11, "symbol": "Na"},
    {"Z": 12, "symbol": "Mg"},
    {"Z": 13, "symbol": "Al"},
    {"Z": 14, "symbol": "Si"},
    {"Z": 15, "symbol": "P"},
    {"Z": 16, "symbol": "S"},
    {"Z": 17, "symbol": "Cl"},
    {"Z": 18, "symbol": "Ar"},
    {"Z": 19, "symbol": "K"},
    {"Z": 20, "symbol": "Ca"},
]

# 세션 상태 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "q_num" not in st.session_state:
    st.session_state.q_num = 0
if "current_element" not in st.session_state:
    st.session_state.current_element = None
if "feedback" not in st.session_state:
    st.session_state.feedback = ""
if "game_over" not in st.session_state:
    st.session_state.game_over = False

def new_question():
    st.session_state.current_element = random.choice(ELEMENTS_1_20)
    st.session_state.feedback = ""

# 처음 로드시 문제 하나 생성
if st.session_state.current_element is None and not st.session_state.game_over:
    new_question()

st.markdown(f"### 🔢 현재 점수: **{st.session_state.score} / {st.session_state.q_num}**")

if st.session_state.game_over:
    st.subheader("🎉 게임 종료!")
    st.write(f"최종 점수: **{st.session_state.score} / 20**")

    if st.button("🔁 다시 시작하기"):
        st.session_state.score = 0
        st.session_state.q_num = 0
        st.session_state.game_over = False
        new_question()
    st.stop()

# 현재 문제 표시
elem = st.session_state.current_element
st.markdown(f"### 문제 {st.session_state.q_num + 1} / 20")
st.write(f"**원자번호 {elem['Z']}번 원소의 기호는?**")

with st.form("quiz_form"):
    answer = st.text_input("원소 기호를 입력하세요 (예: H, He, Na 등)", key="answer")
    submitted = st.form_submit_button("제출")

if submitted:
    user = answer.strip()
    correct = elem["symbol"]

    st.session_state.q_num += 1

    if user.lower() == correct.lower():
        st.session_state.score += 1
        st.session_state.feedback = f"✅ 정답! {elem['Z']}번 원소의 기호는 **{correct}** 입니다."
    else:
        if user == "":
            st.session_state.feedback = f"❌ 미입력! {elem['Z']}번 원소의 기호는 **{correct}** 입니다."
        else:
            st.session_state.feedback = f"❌ 오답! 입력: `{user}`, 정답: **{correct}**"

    # 20문제 끝났는지 확인
    if st.session_state.q_num >= 20:
        st.session_state.game_over = True
    else:
        new_question()

# 피드백 출력
if st.session_state.feedback:
    st.markdown("---")
    st.write(st.session_state.feedback)
