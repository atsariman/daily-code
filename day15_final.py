import streamlit as st
import pandas as pd
import requests
import random

# 1. 페이지 설정 (반드시 맨 첫 줄에 있어야 함)
st.set_page_config(
    page_title="제주 스마트팜 통합 관제",
    page_icon="🍊",
    layout="wide"
)

# 2. 사이드바 메뉴 구성
st.sidebar.title("🚜 스마트팜 시스템")
st.sidebar.info("사용자: 김농부 (관리자)")
menu = st.sidebar.radio("메뉴 이동", ["대시보드", "실시간 날씨", "유통 시세 분석"])

# --- [메뉴 1] 대시보드 (메인 화면) ---
if menu == "대시보드":
    st.title("🏡 농장 현황 대시보드")
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("오늘 방문자", "125명", "+15명")
    col2.metric("주문 대기", "8건", "-2건")
    col3.metric("시스템 상태", "정상 가동", "OK")

    st.success("📢 [알림] 내일 오전 10시에 트랙터 정기 점검이 예약되어 있습니다.")
    st.image("https://images.unsplash.com/photo-1625246333195-58197bd47d26", caption="실시간 농장 CCTV 화면")

# --- [메뉴 2] 실시간 날씨 (API 연동) ---
elif menu == "실시간 날씨":
    st.title("☁️ 기상 관제 센터")
    
    def get_weather():
        url = "https://api.open-meteo.com/v1/forecast?latitude=33.49&longitude=126.53&current_weather=true"
        res = requests.get(url)
        return res.json()['current_weather'] if res.status_code == 200 else None

    if st.button("🔄 날씨 정보 새로고침"):
        st.toast("기상청 서버와 통신 중...")

    weather = get_weather()
    if weather:
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("기온", f"{weather['temperature']}°C")
        with c2:
            st.metric("풍속", f"{weather['windspeed']} km/h")
        with c3:
            st.metric("풍향", f"{weather['winddirection']}°")
        
        st.info(f"데이터 기준 시간: {weather['time']}")

# --- [메뉴 3] 유통 시세 분석 (데이터 시각화) ---
elif menu == "유통 시세 분석":
    st.title("📈 농산물 유통 시세")
    
    data = {
        '날짜': ['1월 1일', '1월 2일', '1월 3일', '1월 4일', '1월 5일'],
        '유기농 콩': [4500, 4200, 4800, 5100, 5300],
        '제주 감귤': [2000, 2100, 1900, 2200, 2500]
    }
    df = pd.DataFrame(data).set_index('날짜')

    tab1, tab2 = st.tabs(["📉 꺾은선 그래프", "📊 막대 그래프"])
    
    with tab1:
        st.line_chart(df)
    with tab2:
        st.bar_chart(df)
