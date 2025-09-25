import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import locale
from utils import load_css

# Configura locale para formato brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def formatar_moeda(valor):
    """Formata número no padrão brasileiro R$ 1.234,56"""
    return locale.currency(valor, grouping=True)


load_dotenv()
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

def ir_para_home():
    st.session_state.pagina_atual = "Home"

def mostrar_report():
    
    load_css()
    
    with st.container():
        col_btn = st.columns([9, 3])[1]
        with col_btn:
            st.button(
                "Home",
                key="btn-home-report",
                on_click=ir_para_home,
                help="Clique para ir para Home"
            )
                

    st.title("Assistente IA para Analistas de Performance Marketing")
    
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    
     # 🔹 Inicializa contador de relatórios na sessão
    if "relatorios_gerados" not in st.session_state:
        st.session_state.relatorios_gerados = 0

    # 🔹 Define limite máximo
    LIMITE = 3  

    orcamento = st.number_input("Digite o orçamento do cliente (R$):", min_value=0.01, step=0.01)
    cpc = st.number_input("Digite o CPC (R$):", min_value=0.01, step=0.01)
    cpa = st.number_input("Digite o CPA (R$):", min_value=0.01, step=0.01)

    if st.button("Gerar análise pela IA"):
        if st.session_state.relatorios_gerados >= LIMITE:
            st.error("🚨 Seu limite de geração de relatórios acabou!")
            return
        prompt = (
            f"Você é um especialista em marketing de performance. "
            f"O cliente possui um orçamento de {formatar_moeda(orcamento)}, "
            f"um CPC de {formatar_moeda(cpc)} e um CPA de {formatar_moeda(cpa)}. "
            f"Gere um texto em HTML simples, usando apenas parágrafos <p>, "
            f"em até 8 linhas. O texto deve: "
            f"- apresentar cliques e leads esperados; "
            f"- mostrar os valores diários, semanais e mensais de investimento, cliques e leads; "
            f"- calcular a taxa de conversão de cliques em leads. "
            f"Use português claro e persuasivo, sem termos técnicos pesados, "
            f"e com foco em transmitir confiança e atrair o cliente. "
            f"Não sugira otimizações, não coloque título, apenas a análise em tom comercial."
        )

        with st.spinner("Processando análise..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "Gere apenas HTML simples com <p> para parágrafos. "
                                   "Não use listas, tabelas, negrito ou caracteres especiais."
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.6
            )

            texto = response.choices[0].message.content.strip()
            st.markdown(texto, unsafe_allow_html=True)
            st.success("Análise gerada com sucesso!")
            
            # 🔹 Incrementa contador
            st.session_state.relatorios_gerados += 1

            st.info(f"📊 Relatórios usados: {st.session_state.relatorios_gerados}/{LIMITE}")
            

        
