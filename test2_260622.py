import streamlit as st
import pandas as pd

df = pd.read_csv(r"D:\python_basic_1wk\st_streamlit_test\heart_failure.csv")

st.subheader("환자데이터")
st.dataframe(df.head())

st.metric(
    label="전체환자 수",
    value=f"{len(df)}명",
    delta="299건 수집"
)