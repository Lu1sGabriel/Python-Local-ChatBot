from langchain_ollama import OllamaLLM
from .prompt_builder import PromptBuilder


class LLMService:
    def __init__(self, model_name="llama3"):
        self.model = OllamaLLM(model=model_name)
        self.prompt_builder = PromptBuilder()
        self.chain = self.prompt_builder.prompt_template | self.model

    def get_response(self, context: str, question: str) -> str:
        prompt_data = self.prompt_builder.build(context, question)
        response = self.chain.invoke(prompt_data)
        return str(response).strip()
