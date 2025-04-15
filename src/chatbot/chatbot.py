from .llm_service import LLMService
from .conversation_storage import ConversationStorage


class ChatBot:
    def __init__(self, user_id: str, conversation_id: str = None, storage: ConversationStorage = None):
        self.user_id = user_id
        self.storage = storage or ConversationStorage()
        self.conversation_id = conversation_id or self.storage.start_conversation(user_id)
        self.llm_service = LLMService()
        self.context = self._load_previous_context()

    def _load_previous_context(self) -> str:
        history = self.storage.load_conversation(self.user_id, self.conversation_id)
        context = ""
        for item in history:
            context += f"\nUser: {item['user_input']}\nAI: {item['bot_response']}"
        return context

    def start(self):
        print(f"🤖 Welcome back, {self.user_id}!")
        print("Type 'exit' to quit.\n")

        while True:
            user_input = input("You: ").strip()
            if user_input.lower() == "exit":
                print("👋 Goodbye!")
                break

            response = self.llm_service.get_response(self.context, user_input)
            print("Bot:", response)

            self.update_context(user_input, response)
            self.storage.save_interaction(self.user_id, self.conversation_id, user_input, response)

    def update_context(self, user_input: str, response: str):
        self.context += f"\nUser: {user_input}\nAI: {response}"
