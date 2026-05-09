import streamlit as st
import json
import time

@st.cache_data
def get_quiz_data():
    # 캐싱 효과를 데모에서 보여주기 위해 의도적으로 지연 시간 추가
    time.sleep(1.5) 
    with open('quiz_data.json', 'r', encoding='utf-8') as f:
        return json.load(f)