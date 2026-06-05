import json
import os

class JsonHelperClass:
    def __init__(self, filename):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.filepath = os.path.join(current_dir, filename)
        self.exists_json()

    def exists_json(self):  
        if not os.path.exists(self.filepath):   
            with open(self.filepath, "w", encoding="utf-8") as file:            
                json.dump([], file) 

    def load_json(self):
        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"[FEHLER] item.json nicht gefunden unter: {self.filepath}")
            return []
        except json.JSONDecodeError:
            print(f"[FEHLER] Die Datei unter {self.filepath} ist kein gültiges JSON Format!")
            return []
        
    def save_json(self, data):
        try:
            with open(self.filepath, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"[FEHLER] Fehler beim Speichern der Datei: {e}")