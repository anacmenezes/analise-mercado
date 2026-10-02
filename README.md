<h1>Análise de Mercado - Multiagente</h1>

<p align="center">
  <a href="#tecnologias">Tecnologias</a> •
  <a href="#practices-adopted">Práticas adotadas</a> •
  <a href="#pre-requisites">Requisitos</a> •
  <a href="#how-to-Installing">Instalando o projeto</a> •
  <a href="#how-to-use">Como executar</a> •
  <a href="#architecture">Arquitetura</a> •
  <a href="#future">Próximos passos</a>
</p>

Essa aplicação foi desenvolvida utilizando **Python e CrewAI** para criação de um sistema de análise de mercado baseado em arquitetura multiagente. O projeto utiliza agentes especializados para coletar, analisar e interpretar informações de mercado, permitindo a construção de uma análise consolidada a partir dos dados disponíveis.

<h2 id="tecnologias">🔌 Tecnologias </h2>

* [Python](https://www.python.org/)
* [CrewAI](https://www.crewai.com/)
* [OpenAI API](https://platform.openai.com/)
* [python-dotenv](https://pypi.org/project/python-dotenv/)

<h2 id="practices-adopted">📖 Práticas adotadas </h2>

* Arquitetura Multiagente
* Separação de responsabilidades
* Orquestração de agentes com CrewAI
* Engenharia de Prompt
* Desenvolvimento modular
* Execução sequencial de tarefas
* Utilização de LLMs
* Análise automatizada de informações
* Variáveis de ambiente para configuração

<h2 id="pre-requisites">💻 Requisitos</h2>

Para rodar esse projeto você precisa ter o Python instalado na sua máquina.

Também é necessário possuir uma chave de API da OpenAI.

* Python 3.10+
* OpenAI API Key

<h2 id="how-to-Installing">🚀 Instalando o projeto</h2>

Primeiro você deve clonar o repositório:

```bash
# Clone o repositório
git clone https://github.com/anacmenezes/analise-mercado.git
```

```bash
# Acesse o projeto
cd analise-mercado
```

Crie o ambiente virtual:

```bash
# Crie o ambiente virtual
python -m venv .venv
```

Ative o ambiente virtual:

```powershell
# Ative o ambiente virtual
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
# Instale as dependências
pip install -r requirements.txt
```

<h2 id="configuration">🔐 Configuração</h2>

Crie um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY=sua_chave_aqui
```

O arquivo `.env` não deve ser enviado para o GitHub.

Utilize as variáveis de ambiente para armazenar informações sensíveis e configurações da aplicação.

<h2 id="how-to-use">💡 Como Executar</h2>

Com o ambiente virtual ativado, execute o projeto:

```bash
python analise_mercado.py
```

Caso o projeto esteja estruturado como módulo Python:

```bash
python -m analise_mercado
```

<h2 id="architecture">🏗️ Arquitetura</h2>

O projeto utiliza uma arquitetura baseada em **múltiplos agentes especializados**, onde cada agente possui uma responsabilidade específica dentro do processo de análise.

```text
                         CLIENTE
                            │
                            ▼
                          CREW
                            │
                            ▼
                    COLETA DE DADOS
                            │
                            ▼
                   ANÁLISE DE MERCADO
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
         AGENTE 1        AGENTE 2        AGENTE 3
             │              │              │
             └──────────────┼──────────────┘
                            ▼
                    CONSOLIDAÇÃO
                            │
                            ▼
                    RELATÓRIO FINAL
```

<h2 id="future">🚀 Próximos passos</h2>

O projeto foi estruturado para receber novas funcionalidades de Engenharia de IA, como:

* Implementação de RAG
* Base de conhecimento própria
* Memória para os agentes
* Utilização de ferramentas externas
* Integração com APIs de dados de mercado
* Validação das respostas
* Redução de alucinações
* Observabilidade
* Monitoramento de custos e tokens
* Testes automatizados
* Persistência de dados
* Melhorias na arquitetura multiagente
* Transformação do notebook em uma aplicação Python modular

<h2 id="author">👩‍💻 Ana Carulina Menezes</h2>

Projeto desenvolvido como parte da construção de portfólio em **Engenharia de IA**, com foco em sistemas multiagentes, LLMs, automação, análise de dados e aplicações utilizando Python e CrewAI.