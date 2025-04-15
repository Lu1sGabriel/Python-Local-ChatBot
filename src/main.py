from uuid import uuid4

from chatbot.chatbot import ChatBot
from chatbot.conversation_storage import ConversationStorage


def ask_choice(prompt, options):
    print(prompt)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    choice = input("Selecione uma opção: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(options):
        return options[int(choice) - 1]
    return None


def main():
    storage = ConversationStorage()

    # Verifica se há usuários salvos
    users = storage.list_users()
    if users:
        choice = ask_choice("Usuário existente encontrado. O que deseja fazer?", [
            "Selecionar um usuário existente",
            "Criar novo usuário"
        ])

        if choice == "Selecionar um usuário existente":
            user_id = ask_choice("Escolha o usuário:", users)
        else:
            user_id = f"user_{uuid4().hex[:8]}"
    else:
        print("Nenhum usuário encontrado, criando novo...")
        user_id = f"user_{uuid4().hex[:8]}"

    # Verifica se há conversas existentes
    conversations = storage.list_conversations(user_id)
    if conversations:
        choice = ask_choice("Conversas encontradas para este usuário. O que deseja fazer?", [
            "Continuar uma conversa existente",
            "Iniciar nova conversa"
        ])

        if choice == "Continuar uma conversa existente":
            conversation_id = ask_choice("Escolha a conversa:", conversations)
        else:
            conversation_id = storage.start_conversation(user_id)
    else:
        print("Nenhuma conversa encontrada. Iniciando nova...")
        conversation_id = storage.start_conversation(user_id)

    # Inicia o chatbot
    bot = ChatBot(user_id=user_id, conversation_id=conversation_id, storage=storage)
    bot.start()


if __name__ == "__main__":
    main()
