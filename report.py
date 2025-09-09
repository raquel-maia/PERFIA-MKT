import streamlit as st
from utils import load_css
import random

def ir_para_home():
    st.session_state.pagina_atual = "Home"

def mostrar_report():
    # Injeta CSS na página
    load_css()
    
    with st.container():
        # Cria duas colunas e pega a segunda para botões
        col_btn = st.columns([9, 3])[1]
        with col_btn:
            # Botão "Home" só com on_click, não precisa chamar de novo
            st.button(
                "Home",
                key="btn-home-report",
                on_click=ir_para_home,
                help="Clique para ir para Home"
            )
                
    # Conteúdo principal
    st.title("Assistente IA para Analistas de Performance Marketing")
    
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    orcamento = st.number_input("Digite o orçamento do cliente (R$):", min_value=0.01, step=0.01)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    cpc = st.number_input("Digite o CPC (R$):", min_value=0.01, step=0.01)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    cpa = st.number_input("Digite o CPA (R$):", min_value=0.01, step=0.01)
    st.markdown('</div>', unsafe_allow_html=True)

 
    if st.button("Gerar análise", key="btn-gerar-analise"):
        respostas_teste = [
            f"Com um orçamento de {orcamento:.2f} reais, sua marca poderá gerar aproximadamente {int(orcamento/cpc)} cliques "
            f"e {int(orcamento/cpa)} leads. Com esse investimento, sua empresa já terá visibilidade relevante no mercado. "
            "Valores maiores poderão ser alcançados conforme o aumento do investimento e campanhas bem direcionadas. "
            "A performance estimada indica que o público-alvo será atingido de forma eficiente. "
            "O número de interações tende a crescer proporcionalmente ao orçamento. "
            "Esses dados demonstram o potencial de alcance da sua marca.",
            
            f"Com um orçamento de {orcamento:.2f} reais, estima-se que sua marca alcance cerca de {int(orcamento/cpc)} cliques "
            f"e {int(orcamento/cpa)} leads. Este investimento proporciona visibilidade inicial e engajamento com o público. "
            "Investimentos maiores, combinados com campanhas bem direcionadas, poderão aumentar esses números. "
            "O potencial de crescimento é evidente. "
            "O impacto no mercado será proporcional ao investimento realizado. "
            "Esses valores mostram o alcance possível da sua marca com o orçamento informado."
        ]
        st.success("Análise gerada (MODO TESTE, sem IA):")
        st.write(random.choice(respostas_teste))
