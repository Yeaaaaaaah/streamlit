# streamlit 라이브러리 호출
import streamlit as st
# 마크다운을 기반으로 한 꾸미기 기능 작동
# 가장 간단한 웹 사이트를 만드는 방법
import pandas as pd
import requests
from datetime import datetime
import pytz
from streamlit.components.v1 import html
seoul_pet_consignment = pd.read_csv("dir/file.csv")
@st.experimental_memo
def convert_df(seoul_pet_consignment):
   return seoul_pet_consignment.to_csv(index=False).encode('utf-8')
csv = convert_df(df)
# def create_df():
#   # DF_URL
#   df_URL = ["https://raw.githubusercontent.com/jaiwon880/Python_bd23_hjw/main/submission/jaiwon880/01_first_webapp/%EB%8F%99%EB%AC%BC%EC%9C%84%ED%83%81%EA%B4%80%EB%A6%AC%EC%97%85.csv",
#   "https://raw.githubusercontent.com/jaiwon880/Python_bd23_hjw/main/submission/jaiwon880/01_first_webapp/%EB%B0%98%EB%A0%A4%EB%8F%99%EB%AC%BC%2B%EC%9C%A0%EB%AC%B4%2B%EB%B0%8F%2B%EC%B7%A8%EB%93%9D%2B%EA%B2%BD%EB%A1%9C_20230314161547.csv",
#   "https://raw.githubusercontent.com/jaiwon880/Python_bd23_hjw/main/submission/jaiwon880/01_first_webapp/%EC%84%9C%EC%9A%B8%EC%8B%9C%20%EC%A3%BC%EC%9A%94%20%EA%B3%B5%EC%9B%90%ED%98%84%ED%99%A9.csv",
#   "https://raw.githubusercontent.com/jaiwon880/Python_bd23_hjw/main/submission/jaiwon880/01_first_webapp/%EC%84%9C%EC%9A%B8%EC%8B%9C%20%EC%95%A0%EA%B2%AC%EB%AF%B8%EC%9A%A9%EC%97%85%EC%9E%A5.csv",
#   "https://raw.githubusercontent.com/jaiwon880/Python_bd23_hjw/main/submission/jaiwon880/01_first_webapp/%EC%84%9C%EC%9A%B8%EC%8B%9C_%EB%8F%99%EB%AC%BC%EB%B3%91%EC%9B%90.csv"]
#   # df을 읽어 오면서 df언네임 삭제
#   df1 = pd.read_csv(df_URL[i]).iloc[:, 1:]
#   # df인덱스 올림
#   df.index += 1
#   # df 반환
#   return df
# seoul_pet_consignment =
# seoul_pet_own =
# seoul_park =
# seoul_pet_hospital =
# seoul_pet_beauty =
st.write(
    """
    ## 팻밀리:느낌표:
    ---
    """
)
st.sidebar.title('서울시 자치구를 선택해주세요:아래를_가리키는_손_모양:')
add_selectbox = st.sidebar.selectbox("자치구 선택",
["강남구", "강동구", "강북구", "강서구", "관악구", "광진구", "구로구", "금천구", "노원구", "도봉구", "동대문구", "동작구", "마포구", "서대문구", "서초구", "성동구", "성북구", "송파구", "양천구", "영등포구", "용산구", "은평구", "종로구", "중구","중랑구"]
)
col1,col2 = st.columns([1,1])
# 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성
with col1 :
  # column 1 에 담을 내용
  st.markdown("**나에게 :blue[가장 도움이 될 것 같은] 유튜브**")
  st.image("https://user-images.githubusercontent.com/71927533/221650828-c1a86b95-99ac-4a85-a4cc-e398eaf2865f.jpg")
  st.info('추천 이유 : 신기하고 재밌는 인공지능을 쉽게, 짧게 설명해주는 유튜브 입니다!', icon=":정보_소스:")
  # Text Area
  message = st.text_area("소개해 드린 추천 채널의 느낀점을 입력해 주세요", "이곳에 입력하세요.")
  if st.button("Submit", key='message'):
    result = message.title()
    st.success(result)
  st.write(
    """
    > 출처: [빵형의 개발도상국](https://www.youtube.com/@bbanghyong/), [노마드 코더](https://www.youtube.com/@nomadcoders)
    """)
with col2 :
  # column 2 에 담을 내용
  st.markdown("**:red[남]이보면 좋을 것 같은 유튜브**")
  st.image("https://user-images.githubusercontent.com/71927533/221631810-b72fa62f-2c41-4a86-a105-2f4a0c1e1b2c.jpg")
  st.info('추천 이유 : IT 트렌드 흐름을 알기 쉽고 빠르게 설명해주고, 간단 명료합니다!', icon=":정보_소스:")