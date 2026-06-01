import json
import random
from repository_base import LootRepository

class LootSystem: 
    def __init__(self, repository: LootRepository):
        self.repository = repository

    def roll_loot(self) -> dict | None:
        item = self.repository.get_all_items()
        if not item:
            return None
        return random.choice(item)
