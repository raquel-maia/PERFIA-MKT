# 📊 PerfIA MKT

**PerfIA MKT** é um projeto que estou desenvolvendo na disciplina **Projeto de Software Impacta**.  
A ideia é criar uma aplicação para **analisar dados de campanhas de marketing digital**, simulando e mostrando métricas como cliques, leads e taxa de conversão de forma fácil de entender.

O projeto vai crescendo aos poucos, com novas funcionalidades sendo adicionadas em cada entrega.

---

## 💡 De onde veio a ideia
Eu trabalhei como analista de marketing de performance e percebi que gerar análises e relatórios rápidos nem sempre era fácil, principalmente com os dados que usamos para mostrar resultados a potenciais clientes.  

O **PerfIA MKT** nasceu para **automatizar isso**, ajudar na tomada de decisões e gerar insights de forma prática e interativa. 💜👩🏽‍💻

---

## 🏗️ Como o projeto está organizado
Mesmo sendo um projeto de análise de dados, ele segue uma estrutura em camadas para deixar tudo organizado:

- **Camada de Dados (Data Layer)**  
  Aqui pegamos os dados das campanhas, processamos e organizamos. É onde acontecem os cálculos de cliques, leads e taxas de conversão — a base pronta para análise.

- **Camada de Lógica (Business Logic / Back-End)**  
  É onde fica a lógica da análise: cálculos, ajustes de médias e geração de insights automáticos com GPT.

- **Camada de Apresentação (Front-End / Interface)**  
  Feita com **Streamlit**, para que qualquer pessoa consiga colocar os valores das campanhas, ver métricas, gráficos e relatórios de forma simples.  
  - O Streamlit também facilita colocar a aplicação online (deploy) e mostrar os resultados sem precisar instalar nada no computador.

---

## 🛠️ Tecnologias que vamos usar
- **Python** → para fazer os cálculos, manipular os dados e integrar tudo.  
- **Streamlit** → para criar a interface web fácil de usar e publicar online.  
- **Plotly** → para gerar gráficos interativos e visualmente legais.  
- **OpenAI GPT** → para gerar relatórios automáticos e insights rápidos.

> ⚠️ Todas as tecnologias ainda vão ser implementadas ao longo do desenvolvimento.

---

## 📐 Funcionalidades previstas
- Estimativa inicial automática de cliques, leads e médias diárias com base em investimento, CPC e CPA, incluindo ajuste da média de leads (+1%).
- Geração automática de relatórios e insights com suporte do GPT.
- Criar gráficos interativos (Plotly) para visualizar os dados.  
- Envio automático de e-mail com o relatório gerado.

---

## 📅 Entregas da disciplina
- **AC1 (14/09):** Configurações iniciais, criação do repositório e atividades no Trello, entrega de vídeo mostrando a funcionalidade inicial (Primeira versão do cálculo de cliques, leads e médias com Streamlit e relatório teste).  
- **AC2 (12/10):**  Relatório gerado com IA.  
- **AC3 (09/11):** Criação dos gráficos interativos.  
- **Entrega Final (30/11):** Projeto completo, refinamentos e apresentação final.

---

## 🚀 Como executar
> Detalhes de instalação e execução serão adicionados conforme as funcionalidades forem implementadas.

---

## 👩🏽‍💻 Eu
- Raquel Maia
