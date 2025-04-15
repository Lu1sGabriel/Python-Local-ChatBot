from langchain_ollama import OllamaLLM

model = OllamaLLM(model="llama3")

ollamaResponse = model.invoke(input="Hello World!")
print(ollamaResponse)
