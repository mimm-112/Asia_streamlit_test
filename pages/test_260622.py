import streamlit as st
# streamlit run 000.py 로 실행 이후에 ---> ctrl + C로 서버 종료할 수 있음

st.title("건강 데이터 탐험기")
st.write("이 앱은 사용자의 건강 데이터를 토대로 관련 정보를 제공합니다.")

name = st.text_input("이름을 입력하세요.")

if name:
    st.write(f"반갑습니다, {name}님! 함께 시작해요")
    
else:
    st.info("위에 이름을 입력하면 인사를 드릴게요!")
    
