# streamlit 라이브러리를 써서 "제주 푸른 콩 농장" 웹사이트 화면 만들어
# 제목, 부제목, 그리고 "환영합니다"라는 본문 글씨를 넣어
# 버튼을 하나 만들어서 누르면 "풍년이네요!"라고 뜨게해
import streamlit as st

st.title("제주 푸른 콩 농장")
st.header("제주 푸른 콩 농장")
st.subheader("제주 푸른 콩 농장")
st.text("환영합니다")
st.button("풍년이네요!")
if st.button("눌러보세요"):
    st.balloons()
    st.write("풍년이네요!")
    st.success("수확량이 2배")