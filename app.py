# -*- coding: utf-8 -*-
import streamlit as st
import streamlit.components.v1 as stc

from login import loginRunApp
from tourism import runApp
from tour_html import tour_html
from about_html import about_html

def main():
  menu = ["Home",'로그인 페이지', '자료분석', 'About']
  choice = st.sidebar.selectbox('메뉴', menu)
  if choice == "Home":
    st.markdown(tour_html, unsafe_allow_html=True)

  elif choice == '로그인 페이지':
    loginRunApp()
  elif choice == '자료분석':
    runApp()
  elif choice == 'About':
    st.markdown(about_html, unsafe_allow_html=True)
  else:
    pass

if __name__ == "__main__":
  main()