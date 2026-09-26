<h1>Analise de Mercado</h1>

<p align="center">
  <a href="#tecnologias">Tecnologias</a> •
  <a href="#practices-adopted">Práticas adotadas</a> •
  <a href="#pre-requisites">Requisitos</a> •
  <a href="#how-to-Installing">Instalando o projeto</a> •
  <a href="#how-to-use">Como executar</a>
</p>

Essa aplicação foi desenvolvida utilizando Python e CrewAI para criação de um sistema de análise de mercado baseado em uma arquitetura Multi-Agent. O sistema utiliza agentes especializados para realizar pesquisas, analisar informações, identificar tendências e gerar insights estratégicos.

<h2 id="tecnologias">🔌 Tecnologias </h2>

* [Python](https://www.python.org/)
* [CrewAI](https://www.crewai.com/)
* [Pydantic](https://docs.pydantic.dev/)
* [Python Dotenv](https://pypi.org/project/python-dotenv/)
* LLM

<h2 id="practices-adopted">📖 Práticas adotadas </h2>

* Arquitetura Multi-Agent
* Separação de responsabilidades
* Orquestração de agentes
* Prompt Engineering
* Task-based workflow
* Uso de ferramentas externas
* Geração de relatórios estruturados
* Variáveis de ambiente

<h2 id="pre-requisites">💻 Requisitos</h2>

Para rodar esse projeto você precisa ter o Python 3.10+ instalado na sua máquina e uma API Key de um provedor de LLM.

<h2 id="how-to-Installing">🚀 Instalando o projeto</h2>

Primeiro você deve clonar o repositório,

```bash
# Clone o repositório
$ git clone https://github.com/anacmenezes/analise-mercado.git

# Acesse-o
$ cd analise-mercado
```

Crie um ambiente virtual:

```bash
$ python -m venv .venv
```

Ative o ambiente virtual:

```bash
# Windows
$ .venv\Scripts\activate
```

Instale as dependências:

```bash
$ pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz do projeto e adicione sua API Key:

```env
OPENAI_API_KEY=sua_api_key
```

<h2 id="how-to-use">💡 Como Executar</h2>

Execute a aplicação:

```bash
$ python main.py
```

O sistema iniciará o fluxo de análise de mercado e executará os agentes especializados de forma colaborativa.

O fluxo da aplicação é composto pelas seguintes etapas:

```text
Market Researcher
        ↓
Market Analyst
        ↓
Market Strategist
        ↓
Report Writer
        ↓
Relatório Final
```

Ao final da execução, será gerado um relatório contendo os principais resultados, tendências e insights identificados durante a análise.
