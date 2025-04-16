from uuid import uuid4

from chatbot.chatbot import ChatBot
from chatbot.conversation_storage import ConversationStorage


def ask_choice(prompt: str, options: list[str]) -> str:
    print(f"\n{prompt}")
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

    while True:
        selection = input("Selecione uma opção: ").strip()
        if selection.isdigit() and 1 <= int(selection) <= len(options):
            return options[int(selection) - 1]
        print("Opção inválida, tente novamente.")


def create_new_user(storage: ConversationStorage) -> tuple[str, str]:
    user_id = f"user_{uuid4().hex[:8]}"
    print(f"Novo usuário criado: {user_id}")
    conversation_id = storage.start_conversation(user_id)
    return user_id, conversation_id


def select_existing_user(storage: ConversationStorage) -> tuple[str, str]:
    user_id = ask_choice("Escolha o usuário:", storage.list_users())
    conversations = storage.list_conversations(user_id)

    if conversations:
        action = ask_choice("Conversas encontradas. O que deseja fazer?", [
            "Continuar uma conversa existente",
            "Iniciar nova conversa"
        ])
        if action == "Continuar uma conversa existente":
            conversation_id = ask_choice("Escolha a conversa:", conversations)
        else:
            conversation_id = storage.start_conversation(user_id)
    else:
        print("Nenhuma conversa encontrada. Iniciando nova...")
        conversation_id = storage.start_conversation(user_id)

    return user_id, conversation_id


def main():
    storage = ConversationStorage()
    users_exist = bool(storage.list_users())

    if not users_exist:
        print("Nenhum usuário encontrado. Criando novo...")
        user_id, conversation_id = create_new_user(storage)
    else:
        action = ask_choice("Usuário existente encontrado. O que deseja fazer?", [
            "Selecionar um usuário existente",
            "Criar novo usuário"
        ])
        if action == "Selecionar um usuário existente":
            user_id, conversation_id = select_existing_user(storage)
        else:
            user_id, conversation_id = create_new_user(storage)

    ChatBot(user_id, conversation_id, storage).start()


if __name__ == "__main__":
    main()
