import streamlit as st
from utils import load_css

def ir_para_report():
    st.session_state.pagina_atual = "Report"

def mostrar_home():
    load_css()
    
    
    # Divide a tela em 2 colunas
    col1, col2 = st.columns([5, 4])

    with col1:
        st.markdown(
        "<h1><span class='titulo-perfia'>PerfIA</span>: Seus dados viram clientes em minutos</h1>",
        unsafe_allow_html=True
    )
        st.button("Comece Aqui", on_click=ir_para_report)
        st.markdown(
            "Bem-vinda(o) ao PerfIA! Aqui você pode inserir dados do cliente e gerar análises de marketing com ajuda da IA."
        )

    with col2:
        st.image("logo.png", width=400)
