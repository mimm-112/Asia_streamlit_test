# app.py — 이 파일만 실행
import streamlit as st
def home():      
    st.title("🏠 홈")
def data():
    st.title("📊 데이터")
pg = st.navigation([
    st.Page(home, title="홈", icon="🏠", default=True),
    st.Page(data, title="데이터",icon="📊")])

pg.run()         
