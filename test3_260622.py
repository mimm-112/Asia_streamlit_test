import streamlit as st
import pandas as pd

df = pd.read_csv("heart_failure.csv")

st.title("심부전 환자 데이터")

st.dataframe(df.head(10))
avg = df['age'].mean()

st.metric("환자 수", f"{len(df)}명")

st.metric("평균 나이", f"{avg:.1f}세")


# st.metric()은 지표를 크게 강조합니다. 여러개는 위에서 아래로 쌓입니다.
# :.1f 는 소수점 첫째자리까지 표시하는 서식입니다.
