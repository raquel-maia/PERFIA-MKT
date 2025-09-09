import streamlit as st

def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        st.markdown(
    """
    <style>
    h1 {
        font-size: 64.6px;
        font-weight: normal;
        color: black;
    }
    .titulo-perfia {
        color: #cdf527;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

