# 💰 Investa — Assistente Virtual Financeira

> Assistente virtual de educação financeira personalizada, desenvolvida em Python com Streamlit e modelo de linguagem local via Ollama.

---

## 📋 Sobre o Projeto

A **Investa** é uma assistente virtual focada em **educação financeira pessoal**. Ela utiliza um modelo de linguagem local (via [Ollama](https://ollama.com/)) para responder dúvidas sobre finanças de forma simples e acolhedora, como se fosse uma amiga explicando para você.

O diferencial da Investa é a **personalização**: ela carrega automaticamente o perfil do investidor, histórico de transações, produtos financeiros disponíveis e histórico de atendimentos para contextualizar cada conversa.

> ⚠️ A Investa **não recomenda investimentos específicos** — seu papel é **educar financeiramente** o usuário, explicando como os produtos e conceitos funcionam.

---

## 🗂️ Estrutura do Projeto

```
financialvirtualassistant/
│
├── data/
│   ├── historico_atendimento.csv     # Histórico de conversas anteriores
│   ├── transacoes.csv                # Últimas transações do cliente
│   ├── perfil_investidor.json        # Perfil, objetivos e patrimônio
│   └── produtos_financeiros.json     # Produtos financeiros disponíveis
│
├── docs/                             # Documentação do projeto
│
├── src/
│   └── app.py                        # Aplicação principal (Streamlit)
│
├── .gitignore
└── README.md
```

---

## 🚀 Tecnologias Utilizadas

| Tecnologia | Uso |
|---|---|
| **Python 3.8+** | Linguagem principal |
| **Streamlit** | Interface de chat web |
| **Ollama** | Execução local do modelo de linguagem |
| **phi4-mini** | Modelo de LLM utilizado |
| **Pandas** | Leitura e manipulação dos dados CSV |
| **Requests** | Comunicação com a API do Ollama |

---

## ⚙️ Pré-requisitos

- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- [Ollama](https://ollama.com/) instalado e rodando localmente
- Modelo `phi4-mini` baixado no Ollama

### Instalar o modelo no Ollama

```bash
ollama pull phi4-mini
```

---

## 🛠️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/Arantesmateus/financialvirtualassistant.git
cd financialvirtualassistant
```

### 2. Crie e ative um ambiente virtual

```bash
# Linux / macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install streamlit pandas requests
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto (se necessário para suas chaves):

```env
# Exemplo
API_KEY=sua_chave_aqui
```

> O `.env` já está listado no `.gitignore` para proteger informações sensíveis.

---

## ▶️ Como Executar

Certifique-se de que o **Ollama está rodando** em segundo plano antes de iniciar a aplicação:

```bash
ollama serve
```

Em seguida, execute a aplicação Streamlit:

```bash
streamlit run src/app.py
```

A interface será aberta automaticamente no navegador em `http://localhost:8501`.

---

## 🤖 Como Funciona

```
┌──────────────┐     pergunta      ┌──────────────────┐
│   Usuário    │ ────────────────► │   Streamlit UI   │
└──────────────┘                   └────────┬─────────┘
                                            │
                                   monta prompt com:
                                   perfil + transações
                                   + histórico + produtos
                                            │
                                            ▼
                                   ┌────────────────────┐
                                   │  Ollama (phi4-mini) │
                                   │   rodando local     │
                                   └────────┬───────────┘
                                            │
                                         resposta
                                            │
                                            ▼
                                   ┌──────────────────┐
                                   │   Chat Investa   │
                                   └──────────────────┘
```

1. O usuário digita uma pergunta no chat
2. A aplicação monta um prompt completo com o **System Prompt** da Investa + **contexto personalizado** do cliente
3. O prompt é enviado para o modelo `phi4-mini` via API local do Ollama
4. A resposta é exibida no chat, mantendo o histórico da conversa na sessão

---

## 📊 Dados do Cliente

O assistente carrega automaticamente 4 fontes de dados:

- **`perfil_investidor.json`** — nome, idade, perfil de risco, objetivo principal, patrimônio e reserva de emergência
- **`transacoes.csv`** — histórico recente de transações financeiras
- **`historico_atendimento.csv`** — atendimentos anteriores para continuidade do contexto
- **`produtos_financeiros.json`** — catálogo de produtos disponíveis para o cliente

---

## 🧠 Comportamento da Investa

A Investa segue regras definidas no System Prompt:

- ✅ Explica como os produtos financeiros funcionam (sem recomendar)
- ✅ Usa linguagem simples e acolhedora
- ✅ Personaliza exemplos com base nos dados reais do cliente
- ✅ Verifica se o cliente possui reserva de emergência
- ✅ Responde de forma sucinta (máximo 3 parágrafos)
- ❌ Não responde perguntas fora do tema de finanças pessoais

---

## 🤝 Contribuindo

1. Faça um **fork** do projeto
2. Crie uma branch (`git checkout -b feature/minha-feature`)
3. Commit suas mudanças (`git commit -m 'feat: adiciona minha feature'`)
4. Push para a branch (`git push origin feature/minha-feature`)
5. Abra um **Pull Request**

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👤 Autor

**Mateus Arantes**

- GitHub: [@Arantesmateus](https://github.com/Arantesmateus)

---

<p align="center">Feito com ❤️, Python e Streamlit</p>
