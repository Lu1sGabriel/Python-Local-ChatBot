from langchain_core.prompts import ChatPromptTemplate


class PromptBuilder:
    TEMPLATE = """Answer the question below. Here is the conversation history:
{context}
Question: {question}
Answer:"""

    def __init__(self):
        self.prompt_template = ChatPromptTemplate.from_template(self.TEMPLATE)

    def build(self, context: str, question: str) -> dict:
        return {
            "context": context.strip(),
            "question": question.strip()
        }
