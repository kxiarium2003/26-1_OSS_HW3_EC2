import streamlit as st
import re
import random
from data_loader import get_quiz_data
from logic import calculate_detailed_report

# 첫 화면 정보 및 과제 명시
st.sidebar.markdown("### OSS 중간고사 대체 과제")
st.sidebar.info(
    "**학번:** 2023510005\n\n"
    "**이름:** 김민지\n"
)

# 세션 상태 초기화
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'quiz_pool' not in st.session_state:
    st.session_state.quiz_pool = None

def login():
    st.title("💰 핀테크·금융 상식 테스트")
    st.markdown("### 🔒 로그인\n\n")
    st.markdown("(아이디: 한글/영문 이름, 비밀번호: 학번 (숫자 10자))")

    with st.container(border=True):
        u_id = st.text_input("아이디 입력")
        u_pw = st.text_input("비밀번호 입력", type="password")
        
        if st.button("분석 시작하기"):
            # 유효성 검사 (실제 로그인 처리)
            if re.fullmatch(r'[a-zA-Z가-힣]+', u_id) and re.fullmatch(r'\d{10}', u_pw):
                st.session_state.logged_in = True
                st.session_state.user_name = u_id
                st.success("인증 성공! 퀴즈 데이터를 생성합니다.")
                st.rerun()
            else:
                st.error("입력 형식을 확인해주세요.")

def quiz():
    st.title(f"{st.session_state.user_name}님의 맞춤형 역량 분석")
    
    # 캐싱 적용된 데이터 로드
    all_questions = get_quiz_data()
    
    # 층화 추출(Stratified Sampling) 로직 구현
    if st.session_state.quiz_pool is None:
        # 카테고리별 분류
        basic_q = [q for q in all_questions if q['type'] == 'basic']
        advanced_q = [q for q in all_questions if q['type'] == 'advanced']
        
        # 기초 2문항 + 심화 3문항 무작위 추출 (총 5문항)
        selected_basic = random.sample(basic_q, 2)
        selected_adv = random.sample(advanced_q, 3)
        
        # 합친 후 순서 섞기
        st.session_state.quiz_pool = selected_basic + selected_adv
        random.shuffle(st.session_state.quiz_pool)
    
    current_quiz = st.session_state.quiz_pool

    # 퀴즈 폼 시작
    with st.form("quiz_form"):
        user_answers = []
        for i, q in enumerate(current_quiz):
            st.markdown(f"**Q{i+1}. {q['question']}**")
            ans = st.radio("정답 선택", q['options'], key=f"q{i}", index=None)
            user_answers.append(ans)
        
        submit = st.form_submit_button("분석 결과 보기")
    
    # 결과 처리 (폼 외부)
    if submit:
        if None in user_answers:
            st.warning("모든 문항에 답변해 주셔야 정확한 분석이 가능합니다.")
        else:
            score = sum(1 for i, q in enumerate(current_quiz) if user_answers[i] == q['answer'])
            report = calculate_detailed_report(score, len(current_quiz))
            
            st.divider()
            st.balloons()
            st.subheader(f"✅ 최종 진단 스코어: {score}/{len(current_quiz)}")
            st.markdown(report)

if not st.session_state.logged_in:
    login()
else:
    if st.sidebar.button("로그아웃"):
        st.session_state.logged_in = False
        st.session_state.quiz_pool = None
        st.rerun()
    quiz()