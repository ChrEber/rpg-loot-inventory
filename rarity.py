import random

def build_rarity_data():
    rarityKeys = ["id", "rarity", "itemRarityValue", "valueMulti", "rarityColor"]
    itemRarity_Liste = [
        [0, "Common", 90, 0.5, "#ffffff"],
        [1, "Uncommon", 60, 1, "#00ff00"],
        [2, "Rare", 30, 3, "#0080ff"],
        [3, "Epic", 10, 5, "#a020f0"],
        [4, "Legendary", 1, 10, "#ff9900"],
    ]
    itemRarity_Dict = [
        dict(zip(rarityKeys, datensatz)) for datensatz in itemRarity_Liste
    ]
    return itemRarity_Dict


def get_weight():
    rarity_DB = build_rarity_data()
    gewichtung = []
    for i in range(len(rarity_DB)):
        gewichtung.append(rarity_DB[i]["itemRarityValue"])
    return gewichtung


def roll_rarity():
    gewichtung = get_weight()
    itemRarity_Dict = build_rarity_data()
    rarity = random.choices(itemRarity_Dict, weights=gewichtung, k=1)
    return rarity
