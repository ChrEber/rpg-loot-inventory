from json_helper import JsonHelperClass
from repository_base import LootRepository

class JsonLootRepository(LootRepository):
    def __init__(self):
        self.helper = JsonHelperClass("items.json")

    def get_all_items(self):
        return self.helper.load_json()
        
