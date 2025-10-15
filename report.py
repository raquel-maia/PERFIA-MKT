import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import locale
import sqlite3
import pandas as pd
from utils import load_css
from graphic import create_performance_analysis_plot

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

    st.markdown("<h1><span class='titulo-perfia'>Assistente IA</span> para Analistas de Mídia</h1>", unsafe_allow_html=True)
    st.markdown('<div class="input-container">', unsafe_allow_html=True)

    # 🔹 Inicializa contador de relatórios na sessão
    if "relatorios_gerados" not in st.session_state:
        st.session_state.relatorios_gerados = 0

    # 🔹 Limite máximo de relatórios
    LIMITE = 3  

    st.markdown("<h4 class='titulo-perfia'>Identificação do Cliente</h4>", unsafe_allow_html=True)

    # 🔹 Conecta ao banco SQLite
    conn = sqlite3.connect("clientes.db")

    # 🔹 Busca lista de clientes
    df_clients = pd.read_sql_query("SELECT client_name FROM clients ORDER BY client_name", conn)
    clientes = df_clients['client_name'].tolist()

    # 🔹 Selectbox começa com opção padrão
    name_lead = st.selectbox("Selecione o cliente:", ["-- Selecione --"] + clientes)

    # 🔹 Inicializa variáveis
    orcamento = cpc = cpa = None

    # 🔹 Só busca dados se cliente selecionado
    if name_lead != "-- Selecione --":
        query = """
            SELECT budget_usd, cpc_usd, cpa_usd
            FROM clients
            WHERE client_name = ?
        """
        dados_cliente = pd.read_sql_query(query, conn, params=(name_lead,))

        if not dados_cliente.empty:
            orcamento = dados_cliente["budget_usd"].iloc[0]
            cpc = dados_cliente["cpc_usd"].iloc[0]
            cpa = dados_cliente["cpa_usd"].iloc[0]

            st.write(f"**Orçamento:** {formatar_moeda(orcamento)}")
            st.write(f"**CPC:** {formatar_moeda(cpc)}")
            st.write(f"**CPA:** {formatar_moeda(cpa)}")
        else:
            st.warning("Nenhum dado encontrado para este cliente.")
    else:
        st.info("Selecione um cliente para carregar os dados.")

    # 🔹 Input da empresa (continua manual)
    name_business = st.text_input("Agência:", placeholder="Digite o nome da sua Agência para agradecimento final..")

    # 🔹 Botão para gerar análise
    if st.button("Gerar análise pela IA"):
        if name_lead == "-- Selecione --" or orcamento is None:
            st.error("Selecione um cliente válido antes de gerar a análise.")
            return

        if st.session_state.relatorios_gerados >= LIMITE:
            st.error("🚨 Seu limite de geração de relatórios acabou!")
            return

        # 🔹 Cálculos básicos
        investimento_diario = orcamento / 30  
        cliques_diario = investimento_diario / cpc  
        leads_diario = investimento_diario / cpa  

        investimento_mensal = orcamento
        cliques_mensal = investimento_mensal / cpc
        leads_mensal = investimento_mensal / cpa

        taxa_conversao = (leads_mensal / cliques_mensal) * 100 if cliques_mensal != 0 else 0

        prompt = (
            f"Você é um especialista em midia de performance marketing e vai enviar uma proposta ao cliente. "
            f"Diga Olá, o nome do cliente é {name_lead}. "
            f"O cliente possui um orçamento de {formatar_moeda(orcamento)}, "
            f"um CPC de {formatar_moeda(cpc)} e um CPA de {formatar_moeda(cpa)}. "
            f"Os cálculos já foram feitos: "
            f"Diariamente: {cliques_diario:.0f} cliques e {leads_diario:.0f} leads. "
            f"Semanalmente: {cliques_diario*7:.0f} cliques e {leads_diario*7:.0f} leads. "
            f"Mensalmente: {cliques_mensal:.0f} cliques e {leads_mensal:.0f} leads. "
            f"A taxa de conversão de cliques em leads é de {taxa_conversao:.0f}%. "
            f"Inclua agradecimento final com o nome da agência que fez análise. Exemplo: agradecemos pela confiança...Atenciosamente {name_business}..  "
            f"Gere um texto em HTML simples usando <p>, em português claro, persuasivo e profissional, "
            f"objetivo, evitando repetições ou elogios exagerados. "
            f"Não use listas, negrito ou caracteres especiais, nem fale que é especialista."
        )

        with st.spinner("Processando análise..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Gere apenas HTML simples com <p> para parágrafos. Não use listas, tabelas, negrito ou caracteres especiais."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.6
            )

            # 🔹 Gera gráfico
            fig = create_performance_analysis_plot(
                investimento_mensal,      
                investimento_diario,    
                cliques_mensal,           
                cliques_diario,           
                leads_diario,             
                leads_mensal               
            )
            st.plotly_chart(fig)

            texto = response.choices[0].message.content.strip()
            st.markdown(texto, unsafe_allow_html=True)
            st.success("Análise gerada com sucesso!")

            # 🔹 Incrementa contador
            st.session_state.relatorios_gerados += 1
            st.info(f"📊 Relatórios usados: {st.session_state.relatorios_gerados}/{LIMITE}")

    # 🔹 Fecha conexão
    conn.close()
