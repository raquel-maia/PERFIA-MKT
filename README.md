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

Mesmo sendo um projeto de análise de dados, ele segue uma estrutura em camadas para manter uma boa organização:

- **Camada de Dados (Data Layer)**  
  Utiliza **SQLite** como banco de dados local, garantindo leveza e praticidade durante o desenvolvimento.  
  Os dados usados para análise são **importados do Kaggle**, simulando campanhas de marketing reais para fins de estudo.  
  Aqui também acontecem os cálculos principais — como estimativas de cliques, leads e taxa de conversão.

- **Camada de Lógica (Business Logic / Back-End)**  
  Contém toda a lógica de negócio: cálculos, ajustes de médias, geração de insights automáticos com GPT e controle de fluxo entre dados e interface.

- **Camada de Apresentação (Front-End / Interface)**  
  Feita com **Streamlit**, para que qualquer pessoa consiga visualizar as métricas, gráficos e relatórios de forma simples e intuitiva.  
  O Streamlit também facilita o *deploy* online, permitindo que o sistema rode diretamente no navegador sem precisar instalar nada localmente.

---

## 🛠 Tecnologias utilizadas

- **Python** — para cálculos, manipulação e integração de dados.  
- **Streamlit** — interface web interativa.  
- **Plotly** — gráficos dinâmicos e interativos.  
- **SQLite** — banco de dados leve e eficiente para armazenar e consultar os dados.  
- **OpenAI GPT** — geração automática de relatórios e insights.  
- **ReportLab** — para gerar relatórios em **PDF** diretamente na aplicação.  
- **Kaggle** — fonte dos dados utilizados nas análises (datasets públicos).

---

## 📐 Funcionalidades

1. Estimativa automática de cliques, leads e médias diárias com base em investimento, CPC e taxa de conversão (com ajuste de média de leads +1%).  
2. Relatórios automáticos com insights gerados via IA (GPT).  
3. Gráficos interativos com Plotly.  
4. Armazenamento de dados em **SQLite**.  
5. Importação de datasets diretamente do **Kaggle**.  
6. **Exportação de relatório em PDF** (nova funcionalidade que substitui o envio por e-mail).

---

## 📅 Entregas previstas na disciplina

- **AC1 (14/09):** Configuração inicial, criação do repositório e das tarefas no Trello, entrega de vídeo com a funcionalidade inicial manual (cálculo de cliques, leads e médias com Streamlit).  
- **AC2 (12/10):** Relatório gerado com IA.  
- **AC3 (09/11):** Gráficos interativos e banco de dados SQLite.  
- **Entrega Final (30/11):** Projeto completo com refinamentos e **geração de relatório em PDF**.


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