import random
import streamlit as st

st.set_page_config(page_title="주기율표 퀴즈", page_icon="🔬")

st.title("🔬 주기율표 게임")
st.write("원자번호를 보고 **원소 기호**를 맞혀보세요! (총 20문제)")

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

# 세션 상태 초기화 (한 번만)
if "initialized" not in st.session_state:
    st.session_state.initialized = True
    # 20문제를 랜덤 순서로 뽑기
    st.session_state.problems = random.sample(ELEMENTS_1_20, k=20)
    st.session_state.idx = 0
    st.session_state.score = 0
    st.session_state.feedback = ""
    st.session_state.game_over = False

score = st.session_state.score
idx = st.session_state.idx
feedback = st.session_state.feedback
game_over = st.session_state.game_over
problems = st.session_state.problems

st.markdown(f"### 🔢 현재 점수: **{score} / {idx}**")

# 게임 끝난 경우
if game_over or idx >= len(problems):
    st.subheader("🎉 게임 종료!")
    st.write(f"최종 점수: **{score} / {len(problems)}**")

    if st.button("🔁 다시 시작하기"):
        st.session_state.initialized = False  # 초기화 플래그 리셋
        st.experimental_rerun()
    st.stop()

# 현재 문제
elem = problems[idx]
st.markdown(f"### 문제 {idx + 1} / {len(problems)}")
st.write(f"**원자번호 {elem['Z']}번 원소의 기호는?**")

with st.form("quiz_form"):
    answer = st.text_input("원소 기호를 입력하세요 (예: H, He, Na 등)", key="answer_input")
    submitted = st.form_submit_button("제출")

if submitted:
    user = answer.strip()
    correct = elem["symbol"]

    # 정답 판정
    if user.lower() == correct.lower():
        st.session_state.score += 1
        st.session_state.feedback = f"✅ 정답! {elem['Z']}번 원소의 기호는 **{correct}** 입니다."
    else:
        if user == "":
            st.session_state.feedback = f"❌ 미입력! {elem['Z']}번 원소의 기호는 **{correct}** 입니다."
        else:
            st.session_state.feedback = f"❌ 오답! 입력: `{user}`, 정답: **{correct}**"

    # 다음 문제로 이동
    st.session_state.idx += 1

    # 마지막 문제였으면 게임 종료 플래그
    if st.session_state.idx >= len(st.session_state.problems):
        st.session_state.game_over = True

    st.experimental_rerun()

# 피드백 출력
if st.session_state.feedback:
    st.markdown("---")
    st.write(st.session_state.feedback)
