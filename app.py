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

if __name__ == "__main__":
  main()