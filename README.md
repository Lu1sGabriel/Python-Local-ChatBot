# 🤖 Chatbot Local com Ollama (LLaMA 3)

Este é um projeto de **chatbot local** feito em **Python**, utilizando o **Ollama** como backend de modelo de linguagem, com suporte ao modelo **LLaMA 3**. Tudo roda **localmente**, usando o seu **processador e placa de vídeo**, sem necessidade de pagar por APIs como OpenAI ou Gemini.

---

## ✨ Principais Características

- Roda totalmente **offline**, com modelos locais.
- Usa **LangChain** para integração com o modelo.
- Armazena **usuários** e **conversas** localmente.
- Suporta múltiplos usuários e histórico de conversa.
- Arquitetura modular e de fácil manutenção.

---

## 🧠 O que é Ollama?

Ollama (anteriormente Ollama) é uma ferramenta que permite rodar modelos de linguagem grandes (LLMs) localmente no seu computador.

Site oficial: [https://ollama.com](https://ollama.com)

---

## ⚙️ Requisitos

- Python 3.10+
- Um computador com performance razoável
  - Preferencialmente com **GPU**
- Espaço livre em disco (modelos podem ocupar de 3 a 10GB)
- Ollama instalado

---

## 🚀 Como Instalar e Rodar

### 1. Clone este repositório

```bash
git clone https://github.com/seu-usuario/chatbot-oylama.git
cd chatbot-oylama
```

### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências Python

```bash
pip install -r requirements.txt
```

Você pode criar o arquivo `requirements.txt` com:

```txt
langchain
langchain-core
langchain-community
langchain-ollama
```

### 4. Instale o Ollama

1. Acesse [https://ollama.com](https://ollama.com)
2. Baixe o instalador e siga os passos na tela.
3. Após instalar, execute no terminal:

```bash
ollama run llama3
```

Isso fará o download e inicialização do modelo **LLaMA 3**.

### 5. Execute o chatbot

```bash
python main.py
```

---

## 🧩 Estrutura do Projeto

```bash
chatbot-oylama/
├── chatbot/
│   ├── chatbot.py               # Lógica principal do bot
│   ├── conversation_storage.py  # Armazena e carrega conversas
│   ├── llm_service.py           # Comunicação com o modelo LLM
│   └── prompt_builder.py        # Constrói o prompt para o modelo
├── resources/
│   └── conversations/           # Onde as conversas são salvas
├── main.py                      # Entrada principal do projeto
├── requirements.txt             # Dependências Python
└── README.md
```

---

## 💬 Como Funciona

1. Ao rodar o programa, você escolhe um usuário ou cria um novo.
2. Escolhe iniciar uma nova conversa ou continuar uma antiga.
3. Digita sua pergunta e recebe uma resposta da IA.
4. Todo o histórico é salvo automaticamente em arquivos `.json`.

---

## 🧪 Exemplo de Uso

```bash
python main.py

🤖 Bem-vindo!
1. Selecionar usuário existente
2. Criar novo usuário
> 2

Novo usuário criado: user_abcd1234

1. Iniciar nova conversa
> 1

You: O que é inteligência artificial?
Bot: Inteligência artificial é o campo da ciência...
```

---

## ❓ Dúvidas Frequentes

**1. Posso usar outro modelo além do LLaMA 3?**  
Sim! Basta alterar o nome do modelo na classe `LLMService`:

```python
class LLMService:
    def __init__(self, model_name: str = "mistral"):
        ...
```

Depois, rode no terminal:

```bash
ollama run mistral
```

**2. E se minha máquina for fraca?**  
Você pode testar modelos mais leves como:

```bash
ollama run llama2
ollama run gemma
```

---

## 🛠 Sugestões Futuras

- Interface gráfica com Tkinter ou PyQt.
- API web com FastAPI.
- Suporte a múltiplos modelos selecionáveis na inicialização.

---

## 🙋‍♂️ Autor

Feito com dedicação e código limpo por Luis Gabriel Goés.

---
