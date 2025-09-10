# 📊 PerfIA MKT

**PerfIA MKT** é um projeto que estou desenvolvendo na disciplina **Projeto de Software Impacta**.  
A ideia é criar uma aplicação para **analisar dados de campanhas de marketing digital**, simulando e mostrando métricas como cliques, leads e taxa de conversão de forma fácil de entender.

O projeto vai crescendo aos poucos, com novas funcionalidades sendo adicionadas a cada entrega.

---

## 💡 De onde veio a ideia

Eu trabalhei como analista de marketing de performance e percebi que gerar análises e relatórios rápidos nem sempre era fácil — especialmente com os dados que usamos para mostrar resultados a clientes.  
O **PerfIA MKT** nasceu para **automatizar isso**, ajudando na tomada de decisões e gerando insights de forma prática e interativa. 💜👩🏽‍💻

---

## 🏗 Como o projeto está organizado

Mesmo sendo um projeto de análise de dados, ele segue uma estrutura em camadas para ficar bem organizado:

- **Camada de Dados (Data Layer)**  
  Recebe os dados das campanhas, processa e organiza. Aqui acontecem os cálculos de cliques, leads e taxa de conversão — a base da análise.

- **Camada de Lógica (Business Logic / Back-End)**  
  Contém a lógica da análise: cálculos, ajustes de média e geração de insights automáticos com GPT.

- **Camada de Apresentação (Front-End / Interface)**  
  Feita com **Streamlit**, para que qualquer pessoa consiga inserir os dados das campanhas e ver métricas, gráficos e relatórios de forma simples.  
  O Streamlit também facilita fazer *deploy* online — você pode mostrar o sistema rodando sem precisar instalar nada no computador de quem estiver vendo.

---

## 🛠 Tecnologias planejadas

- **Python** — para cálculos, manipulação de dados e integração geral.  
- **Streamlit** — para criar uma interface web interativa de maneira simples.  
- **Plotly** — para gerar gráficos interativos e visualmente atrativos.  
- **OpenAI GPT** — para gerar relatórios automáticos e insights.
- **smtplib** — para enviar e-mails com os relatórios gerados.

> ⚠️ Todas essas tecnologias serão implementadas conforme avançamos com o desenvolvimento.

---

## 📐 Funcionalidades previstas

1. Estimativa automática de cliques, leads e médias diárias com base em investimento, CPC e taxa de conversão; com ajuste de média de leads (+1%).  
2. Relatórios automáticos com insights gerados via IA (GPT).  
3. Gráficos interativos usando Plotly para visualização de dados.  
4. Envio automático de relatório por e-mail (smtplib).

---

## 📅 Entregas previstas na disciplina

- **AC1 (14/09):** Configuração inicial, criação do repositório e das tarefas no Trello, entrega de vídeo com a funcionalidade inicial (cálculo de cliques, leads e médias com Streamlit).  
- **AC2 (12/10):** Relatório gerado com IA.  
- **AC3 (09/11):** Gráficos interativos.  
- **Entrega Final (30/11):** Projeto completo com refinamentos, envio de relatório por e-mail e apresentação final.

---

## 🚀 Como executar (por enquanto, versão inicial)

### 1. Clone o repositório
```bash
git clone <URL do seu repositório>
cd perfia-mkt
```
### 2. Crie e ative um ambiente virtual (recomendado)
```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate
```
### 3. Instale as dependências
```bash
pip install -r requirements.txt
```
### 4. Execute a aplicação com Streamlit
```bash
streamlit run app.py
```
## 👩🏽‍💻 Eu 

- Raquel Maia