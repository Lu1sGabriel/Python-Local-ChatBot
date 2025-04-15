from .llm_service import LLMService


class ChatBot:
    def __init__(self):
        self.context = ""
        self.llm_service = LLMService()

    def start(self):
        print("🤖 Welcome to the AI ChatBot! Type 'exit' to quit.")
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() == "exit":
                print("👋 Goodbye!")
                break

            response = self.llm_service.get_response(self.context, user_input)
            print("Bot:", response)
            self.update_context(user_input, response)

    def update_context(self, user_input: str, response: str):
        self.context += f"\nUser: {user_input}\nAI: {response}"
