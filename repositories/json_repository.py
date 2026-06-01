import json
import os

from repository_base import LootRepository

class JsonLootRepository(LootRepository):
    def __init__(self, filename: str = "items.json"):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.filepath = os.path.join(current_dir, filename)

    def get_all_items(self) -> list[dict]:
        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"[FEHLER] item.json nicht gefunden unter: {self.filepath}")
            return []
        except json.JSONDecodeError:
            print(f"[FEHLER] Die Datei unter {self.filepath} ist kein gültiges JSON Format!")
            return []
