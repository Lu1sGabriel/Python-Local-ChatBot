from uuid import uuid4

from chatbot.chatbot import ChatBot
from chatbot.conversation_storage import ConversationStorage


def ask_choice(prompt: str, options: list[str]) -> str:
    print(prompt)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        choice = input("Selecione uma opção: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print("Opção inválida, tente novamente.")


def create_new_user(storage: ConversationStorage) -> tuple[str, str]:
    user_id = f"user_{uuid4().hex[:8]}"
    print(f"Novo usuário criado: {user_id}")
    conversation_id = storage.start_conversation(user_id)
    return user_id, conversation_id


def main():
    storage = ConversationStorage()
    users = storage.list_users()

    if users:
        action = ask_choice("Usuário existente encontrado. O que deseja fazer?", [
            "Selecionar um usuário existente",
            "Criar novo usuário"
        ])

        user_id = ask_choice("Escolha o usuário:", users) if action == "Selecionar um usuário existente" \
            else create_new_user(storage)[0]

    else:
        print("Nenhum usuário encontrado, criando novo...")
        user_id, conversation_id = create_new_user(storage)
        ChatBot(user_id, conversation_id, storage).start()
        return

    conversations = storage.list_conversations(user_id)
    if conversations:
        action = ask_choice("Conversas encontradas. O que deseja fazer?", [
            "Continuar uma conversa existente",
            "Iniciar nova conversa"
        ])
        conversation_id = ask_choice("Escolha a conversa:", conversations) if action == "Continuar uma conversa existente" \
            else storage.start_conversation(user_id)
    else:
        print("Nenhuma conversa encontrada. Iniciando nova...")
        conversation_id = storage.start_conversation(user_id)

    ChatBot(user_id, conversation_id, storage).start()


if __name__ == "__main__":
    main()
