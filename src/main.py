from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define o template de prompt com placeholders que serão preenchidos dinamicamente
template = """
Answer the question below.

Here is the conversation history:
{context}

Question:
{question}

Answer:
"""

# Criação do modelo e template do prompt
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)

# Criação da cadeia (prompt -> modelo)
chain = prompt | model

# Executa a cadeia com os valores fornecidosf
response = chain.invoke({
    "context": "",
    "question": "Hey, how are you?"
})

# Exibe a resposta
print(response)
