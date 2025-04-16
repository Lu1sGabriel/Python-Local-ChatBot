from langchain_core.prompts import ChatPromptTemplate


class PromptBuilder:
    TEMPLATE = """You are a helpful and conversational AI assistant. Based on the conversation history below, answer the user's latest question as clearly and helpfully as possible.

Conversation History:
{context}

User's Question:
{question}

Your Answer:"""

    def __init__(self):
        self.prompt_template = ChatPromptTemplate.from_template(self.TEMPLATE)

    def build(self, context: str, question: str) -> dict:
        return {
            "context": context.strip(),
            "question": question.strip()
        }
