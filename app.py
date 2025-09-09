import streamlit as st
from home import mostrar_home
from report import mostrar_report
from utils import load_css

load_css()

if "pagina_atual" not in st.session_state:
    st.session_state.pagina_atual = "Home"

if st.session_state.pagina_atual == "Home":
    mostrar_home()
elif st.session_state.pagina_atual == "Report":
    mostrar_report()
