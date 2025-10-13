import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import locale
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

    # 🔹 Define limite máximo
    LIMITE = 3  
    st.markdown("<h4 class='titulo-perfia'>Identificação do Cliente</h4>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        name_lead = st.text_input("Cliente:", placeholder="Digite o nome do Cliente..")
    with col2:
        name_business = st.text_input("Empresa:", placeholder="Digite o nome da sua Agência..")
    
    st.markdown("<h4 class='titulo-perfia'>Informações de Campanha</h4>", unsafe_allow_html=True)
    st.caption("Preencha os dados abaixo para gerar o relatório:")
    orcamento = st.number_input("Digite o orçamento do cliente (R$):", min_value=0.01, step=0.01)
    cpc = st.number_input("Digite o CPC (R$):", min_value=0.01, step=0.01)
    cpa = st.number_input("Digite o CPA (R$):", min_value=0.01, step=0.01)

    if st.button("Gerar análise pela IA"):
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
        # 🔹 Calcula taxa de conversão de cliques em leads
        if cliques_mensal != 0:
            taxa_conversao = (leads_mensal / cliques_mensal) * 100
        else:
            taxa_conversao = 0
        
        prompt = (
            f"Você é um especialista em midia de performance marketing e vai enviar uma proposta ao cliente. "
            f"Diga Olá é o nome do cliente é {name_lead}. "
            f"O cliente possui um orçamento de {formatar_moeda(orcamento)}, "
            f"um CPC de {formatar_moeda(cpc)} e um CPA de {formatar_moeda(cpa)}. "
            f"Os cálculos já foram feitos: "
            f"Diariamente: {cliques_diario:.0f} cliques e {leads_diario:.0f} leads. "
            f"Semanalmente: {cliques_diario*7:.0f} cliques e {leads_diario*7:.0f} leads. "
            f"Mensalmente: {cliques_mensal:.0f} cliques e {leads_mensal:.0f} leads. "
            f"A taxa de conversão de cliques em leads é de {taxa_conversao:.0f}%. "
            f"Gere um texto em HTML simples usando <p>, em português claro, persuasivo e profissional, "
            f"objetivo, evitando repetições ou elogios exagerados. "
            f"Inclua agradecimento final. Exemplo: nós da 'coloque o nome da empresa' {name_business} agradecemos pela confiança... "
            f"Não use listas, negrito ou caracteres especiais, nem fale que é especialista."
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
            
            
            
            #st.write("📊 Debug:", investimento_diario, investimento_mensal, cliques_diario, cliques_mensal, leads_diario, leads_mensal)

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
            

        
