# import streamlit as st
# import pandas as pd
# df = pd.read_csv("heart_failure.csv")

############################################################################
# # 슬라이더가 고른 나이가 age_max 로
# age_max = st.slider("최대 나이", 40, 95, 70) # 맨 뒤에 70을 초기값으로 설정해뒀음

# # 선택값으로 데이터를 걸러냄
# filtered = df[df['age'] <= age_max]

# st.write(f"{len(filtered)}명이 조건에 맞습니다")
# st.dataframe(filtered)

############################################################################

# # sex 컬럼: 1=남성, 0=여성
# choice = st.selectbox("성별", ["남성", "여성"])


# code = 1 if choice == "남성" else 0
# result = df[df['sex'] == code]


# only_death = st.checkbox("사망 환자만 보기")
# if only_death:
#     result = result[result['DEATH_EVENT'] == 1]
    
# st.write(f"조건에 맞는 환자: {len(result)}명")
# st.dataframe(result)

############################################################################
# 나이 분포 히스토그램

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("heart_failure.csv")

# fig, ax = plt.subplots()
# ax.hist(df['age'], bins=20, color="#26727AC1")
# ax.set_xlabel("age")
# ax.set_ylabel("count")

# st.pyplot(fig)


############################################################################

# 사망 여부 막대그래프
# 한글 깨짐방지 코드 추가

# import matplotlib.pyplot as plt
# plt.rcParams['font.family'] = 'Malgun Gothic' # Windows
# plt.rcParams['axes.unicode_minus'] = False

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("heart_failure.csv")

# counts = df['DEATH_EVENT'].value_counts().sort_index()

# fig, ax = plt.subplots()

# ax.bar(['생존', '사망'], counts, color=["#10B0E0BA", "#E83DA16A"])
# ax.set_title("생존 vs 사망 환자 수")
# ax.set_ylabel("환자 수")
# st.pyplot(fig)

############################################################################
# 레이아웃구성
# 화면을보기좋게나누기
# 공간을 나누는 도구들 
# col1, col2 = st.columns(2), st.sidebar.slider(...), t1, t2 = st.tabs([...])
# 화면 좌우분할, 왼쪽 고정패널(필터영역), 탭으로 화면전환

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("heart_failure.csv")

# 왼쪽 사이드바에 필터를 둔다
st.sidebar.header("필터")
age = st.sidebar.slider("최대 나이",40, 95, 70)
df = df[df['age'] <= age]

# 본문을 둘로 나눈다
c1, c2 = st.columns(2)
c1.metric("환자 수", len(df))
c2.metric("평균 나이", f"{df.age.mean():.0f}")

# ‘표보기’와‘차트보기’ 두 개의 탭으로 화면을 나눠 보세요.
tab1, tab2 = st.tabs(["📋 표 보기", "📊 차트 보기"])
with tab1:
    st.dataframe(df)
    
with tab2:
    fig, ax = plt.subplots()
    ax.hist(df['age'], bins=20, color='#5BAFB8')
    st.pyplot(fig)

