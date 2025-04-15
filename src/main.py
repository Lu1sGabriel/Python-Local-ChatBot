from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Template do prompt com placeholders dinâmicos
template = """
Answer the question below.

Here is the conversation history:
{context}

Question:
{question}

Answer:
"""

# Instancia o modelo e o template
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)

# Cria a cadeia: prompt -> modelo
chain = prompt | model


def handle_conversation():
    context = ""
    print("🤖 Welcome to the AI ChatBot! Type 'exit' to quit.")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break

        response = chain.invoke({
            "context": context,
            "question": user_input
        })

        print("Bot:", str(response).strip())
        context += f"\nUser: {user_input}\nAI: {response}"


if __name__ == "__main__":
    handle_conversation()
