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

<p>
Essa aplicação foi desenvolvida utilizando <strong>Python e CrewAI</strong>
para criação de um sistema de análise de mercado baseado em arquitetura
multiagente.
</p>

<p>
O objetivo do projeto é demonstrar, na prática, conceitos de
<strong>Engenharia de IA</strong>, como:
</p>

<ul>
  <li>Sistemas multiagentes</li>
  <li>RAG (Retrieval-Augmented Generation)</li>
  <li>LLMs</li>
  <li>Engenharia de prompts</li>
  <li>Uso de ferramentas externas</li>
  <li>Avaliação de agentes</li>
  <li>Observabilidade</li>
  <li>Arquitetura modular</li>
  <li>Tratamento de erros</li>
</ul>

<h2 id="tecnologias">🔌 Tecnologias </h2>

- [Python](https://www.python.org/)
- [CrewAI](https://www.crewai.com/)
- [OpenAI API](https://platform.openai.com/)
- [LangChain](https://www.langchain.com/)
- [ChromaDB](https://www.trychroma.com/)
- [RAG](https://python.langchain.com/docs/concepts/rag/)
- [Serper API](https://serper.dev/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

<h2 id="practices-adopted">📖 Práticas adotadas </h2>

* Arquitetura Multiagente
* Separação de responsabilidades
* Orquestração de agentes com CrewAI
* Engenharia de Prompt
* Desenvolvimento modular
* Execução sequencial de tarefas
* Utilização de LLMs
* Variáveis de ambiente para configuração
* RAG para consulta de conhecimento interno
* Busca de informações externas
* Avaliação de qualidade do relatório
* Observabilidade da execução
* Tratamento de erros

<h2 id="pre-requisites">💻 Requisitos</h2>

Para rodar esse projeto você precisa ter o Python instalado na sua máquina.

Também é necessário possuir uma chave de API da OpenAI.

* Python 3.10+
* OpenAI API Key
* Serper API Key

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
python main.py
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
                   PESQUISADOR DE MERCADO
                      │             │
                      ▼             ▼
                     RAG       BUSCA EXTERNA
                      │             │
                      └──────┬──────┘
                             ▼
                    COLETA DE DADOS
                             │
                             ▼
                    ANALISTA DE TENDÊNCIAS
                             │
                             ▼
                    REDATOR DE RELATÓRIO
                             │
                             ▼
                      RELATÓRIO FINAL
                             │
                ┌────────────┴────────────┐
                ▼                         ▼
          AVALIAÇÃO                 OBSERVABILIDADE
```
<h2 id="evaluation">📊 Avaliação dos agentes</h2>

<p>
O projeto possui uma camada de avaliação para verificar automaticamente
a qualidade das respostas produzidas pelos agentes.
</p>

<p>
As tarefas são avaliadas com base em critérios específicos, como:
</p>

<ul>
  <li>Presença de fontes</li>
  <li>Presença de dados</li>
  <li>Identificação de tendências</li>
  <li>Oportunidades</li>
  <li>Desafios</li>
  <li>Estrutura do relatório</li>
  <li>Conclusão</li>
</ul>

<p>
Cada tarefa recebe uma pontuação baseada nos critérios atendidos.
</p>


<h2 id="observability">🔎 Observabilidade</h2>

<p>
O projeto também possui mecanismos de observabilidade para acompanhar
a execução do fluxo multiagente.
</p>

<p>
São acompanhadas informações como:
</p>

<ul>
  <li>Execução das tarefas</li>
  <li>Resultado produzido por cada agente</li>
  <li>Status das avaliações</li>
  <li>Qualidade do relatório final</li>
  <li>Erros durante a execução</li>
</ul>


<h2 id="rag">🧠 RAG</h2>

<p>
O sistema utiliza <strong>Retrieval-Augmented Generation (RAG)</strong>
para consultar uma base de conhecimento interna antes de realizar
pesquisas externas.
</p>

<p>
Os documentos são processados, transformados em embeddings e armazenados
no <strong>ChromaDB</strong>. Durante a execução, o agente pesquisador
pode recuperar informações relevantes utilizando uma ferramenta própria
de busca RAG.
</p>

<h2 id="future">🚀 Próximos passos</h2>

O projeto foi estruturado para receber novas funcionalidades de Engenharia de IA, como:

* Monitoramento de custos e tokens
* Testes automatizados mais abrangentes
* Persistência de dados
* Melhorias na arquitetura multiagente

<h2 id="author">👩‍💻 Ana Carulina Menezes</h2>

Projeto desenvolvido como parte da construção de portfólio em **Engenharia de IA**, com foco em sistemas multiagentes, LLMs, automação, análise de dados e aplicações utilizando Python e CrewAI.