{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOtih9BE3ajrFfp61oYGOUe",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Yeaaaaaaah/streamlit/blob/main/streamlit.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "kOCHme3R9Zbs",
        "outputId": "f761a675-07c5-41d7-c331-0e6d67bcd72f",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 394
        }
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-1-3f72d0618d90>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# streamlit 라이브러리 호출\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mstreamlit\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mst\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m \u001b[0;31m# 마크다운을 기반으로 한 꾸미기 기능 작동\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;31m# 가장 간단한 웹 사이트를 만드는 방법\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'streamlit'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ],
      "source": [
        "# streamlit 라이브러리 호출\n",
        "import streamlit as st\n",
        "# 마크다운을 기반으로 한 꾸미기 기능 작동\n",
        "# 가장 간단한 웹 사이트를 만드는 방법\n",
        "import pandas as pd\n",
        "import requests\n",
        "from datetime import datetime\n",
        "import pytz\n",
        "from streamlit.components.v1 import html\n",
        "seoul_pet_consignment = pd.read_csv(\"dir/file.csv\")\n",
        "@st.experimental_memo\n",
        "def convert_df(seoul_pet_consignment):\n",
        "   return seoul_pet_consignment.to_csv(index=False).encode('utf-8')\n",
        "csv = convert_df(df)\n",
        "# def create_df():\n",
        "#   # DF_URL\n",
        "#   df_URL = [\"https://raw.githubusercontent.com/jaiwon880/Python_bd23_hjw/main/submission/jaiwon880/01_first_webapp/%EB%8F%99%EB%AC%BC%EC%9C%84%ED%83%81%EA%B4%80%EB%A6%AC%EC%97%85.csv\",\n",
        "#   \"https://raw.githubusercontent.com/jaiwon880/Python_bd23_hjw/main/submission/jaiwon880/01_first_webapp/%EB%B0%98%EB%A0%A4%EB%8F%99%EB%AC%BC%2B%EC%9C%A0%EB%AC%B4%2B%EB%B0%8F%2B%EC%B7%A8%EB%93%9D%2B%EA%B2%BD%EB%A1%9C_20230314161547.csv\",\n",
        "#   \"https://raw.githubusercontent.com/jaiwon880/Python_bd23_hjw/main/submission/jaiwon880/01_first_webapp/%EC%84%9C%EC%9A%B8%EC%8B%9C%20%EC%A3%BC%EC%9A%94%20%EA%B3%B5%EC%9B%90%ED%98%84%ED%99%A9.csv\",\n",
        "#   \"https://raw.githubusercontent.com/jaiwon880/Python_bd23_hjw/main/submission/jaiwon880/01_first_webapp/%EC%84%9C%EC%9A%B8%EC%8B%9C%20%EC%95%A0%EA%B2%AC%EB%AF%B8%EC%9A%A9%EC%97%85%EC%9E%A5.csv\",\n",
        "#   \"https://raw.githubusercontent.com/jaiwon880/Python_bd23_hjw/main/submission/jaiwon880/01_first_webapp/%EC%84%9C%EC%9A%B8%EC%8B%9C_%EB%8F%99%EB%AC%BC%EB%B3%91%EC%9B%90.csv\"]\n",
        "#   # df을 읽어 오면서 df언네임 삭제\n",
        "#   df1 = pd.read_csv(df_URL[i]).iloc[:, 1:]\n",
        "#   # df인덱스 올림\n",
        "#   df.index += 1\n",
        "#   # df 반환\n",
        "#   return df\n",
        "# seoul_pet_consignment =\n",
        "# seoul_pet_own =\n",
        "# seoul_park =\n",
        "# seoul_pet_hospital =\n",
        "# seoul_pet_beauty =\n",
        "st.write(\n",
        "    \"\"\"\n",
        "    ## 팻밀리:느낌표:\n",
        "    ---\n",
        "    \"\"\"\n",
        ")\n",
        "st.sidebar.title('서울시 자치구를 선택해주세요:아래를_가리키는_손_모양:')\n",
        "add_selectbox = st.sidebar.selectbox(\"자치구 선택\",\n",
        "[\"강남구\", \"강동구\", \"강북구\", \"강서구\", \"관악구\", \"광진구\", \"구로구\", \"금천구\", \"노원구\", \"도봉구\", \"동대문구\", \"동작구\", \"마포구\", \"서대문구\", \"서초구\", \"성동구\", \"성북구\", \"송파구\", \"양천구\", \"영등포구\", \"용산구\", \"은평구\", \"종로구\", \"중구\",\"중랑구\"]\n",
        ")\n",
        "col1,col2 = st.columns([1,1])\n",
        "# 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성\n",
        "with col1 :\n",
        "  # column 1 에 담을 내용\n",
        "  st.markdown(\"**나에게 :blue[가장 도움이 될 것 같은] 유튜브**\")\n",
        "  st.image(\"https://user-images.githubusercontent.com/71927533/221650828-c1a86b95-99ac-4a85-a4cc-e398eaf2865f.jpg\")\n",
        "  st.info('추천 이유 : 신기하고 재밌는 인공지능을 쉽게, 짧게 설명해주는 유튜브 입니다!', icon=\":정보_소스:\")\n",
        "  # Text Area\n",
        "  message = st.text_area(\"소개해 드린 추천 채널의 느낀점을 입력해 주세요\", \"이곳에 입력하세요.\")\n",
        "  if st.button(\"Submit\", key='message'):\n",
        "    result = message.title()\n",
        "    st.success(result)\n",
        "  st.write(\n",
        "    \"\"\"\n",
        "    > 출처: [빵형의 개발도상국](https://www.youtube.com/@bbanghyong/), [노마드 코더](https://www.youtube.com/@nomadcoders)\n",
        "    \"\"\")\n",
        "with col2 :\n",
        "  # column 2 에 담을 내용\n",
        "  st.markdown(\"**:red[남]이보면 좋을 것 같은 유튜브**\")\n",
        "  st.image(\"https://user-images.githubusercontent.com/71927533/221631810-b72fa62f-2c41-4a86-a105-2f4a0c1e1b2c.jpg\")\n",
        "  st.info('추천 이유 : IT 트렌드 흐름을 알기 쉽고 빠르게 설명해주고, 간단 명료합니다!', icon=\":정보_소스:\")"
      ]
    }
  ]
}