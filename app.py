# -*- coding: utf-8 -*-
import streamlit as st
import streamlit.components.v1 as stc

from login import loginRunApp
from tour_html import tour_html


def main():
  menu = ["Home",'로그인 페이지', 'About']
  choice = st.sidebar.selectbox('메뉴', menu)
  if choice == "Home":
    st.markdown(tour_html, unsafe_allow_html=True)

  elif choice == '로그인 페이지':
    loginRunApp()

  elif choice == 'About':
    st.title("정보를 확인할 수 없습니다.")
    st.write("분석 결과를 확인하고 싶으시면 로그인을 해주세요.")

  else:
    pass

if __name__ == "__main__":
  main()