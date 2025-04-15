import json
import os
from datetime import datetime
from typing import List, Dict
from uuid import uuid4


class ConversationStorage:
    def __init__(self, base_path="resources/conversations"):
        self.base_path = base_path
        os.makedirs(base_path, exist_ok=True)

    def _get_user_path(self, user_id: str) -> str:
        path = os.path.join(self.base_path, user_id)
        os.makedirs(path, exist_ok=True)
        return path

    def start_conversation(self, user_id: str) -> str:
        conv_id = f"conversation_{datetime.now().strftime('%Y%m%d%H%M%S')}_{uuid4().hex[:8]}"
        file_path = os.path.join(self._get_user_path(user_id), f"{conv_id}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump([], f, indent=2, ensure_ascii=False)
        return conv_id

    def save_interaction(self, user_id: str, conversation_id: str, user_input: str, bot_response: str):
        file_path = os.path.join(self._get_user_path(user_id), f"{conversation_id}.json")
        data = []

        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

        data.append({
            "user_input": user_input,
            "bot_response": bot_response,
            "timestamp": datetime.now().isoformat()
        })

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def list_conversations(self, user_id: str) -> List[str]:
        path = self._get_user_path(user_id)
        return [file.replace(".json", "") for file in os.listdir(path) if file.endswith(".json")]

    def load_conversation(self, user_id: str, conversation_id: str) -> List[Dict[str, str]]:
        file_path = os.path.join(self._get_user_path(user_id), f"{conversation_id}.json")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def list_users(self) -> List[str]:
        return [name for name in os.listdir(self.base_path) if os.path.isdir(os.path.join(self.base_path, name))]
