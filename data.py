from loot import LootSystem
from rarity import roll_rarity
from repositories.json_repository import JsonLootRepository

def generate_loot():
    value = 0
    repository = JsonLootRepository()
    lootSys = LootSystem(repository)
    loot = lootSys.roll_loot()
    rarityGrade = roll_rarity()
    value = loot["baseValue"] * rarityGrade[0]["valueMulti"]
    return {
        "loot": loot["name"],
        "rarityName": rarityGrade[0]["rarity"],
        "value": value,
        "rarityColor": rarityGrade[0]["rarityColor"]
    }
