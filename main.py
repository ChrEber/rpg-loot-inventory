# itemclass:
# 0 = misc
# 1 = weapon
# 2 = armor
# 3 = consumables
# 4 = materials

import json
import random

def load_items():
    with open('items.json','r') as file:
        items = json.load(file)
    return items

def roll_loot():
    item = load_items()
    loot = random.choice(item)
    return loot

def build_rarity_data ():
    itemRarity_Liste = {}
    rarityKeys = ['id', 'rarity', 'itemRarityValue', 'valueMulti', 'rarityColor']
    itemRarity_Liste = [
    	[0, "Common",    90, 0.5, "#ffffff"],
    	[1, "Uncommon",  60,   1, "#00ff00"],
    	[2, "Rare",      30,   3, "#0080ff"],
    	[3, "Epic",      10,   5, "#a020f0"],
    	[4, "Legendary",  1,  10, "#ff9900"]
    ]
    itemRarity_Dict = [dict(zip(rarityKeys, datensatz)) for datensatz in itemRarity_Liste]
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
    rarity = random.choices(itemRarity_Dict, weights = gewichtung, k = 1)
    return rarity

def generate_loot():
    value = 0
    loot = roll_loot()
    rarityGrade = roll_rarity()
    value = loot['baseValue'] * rarityGrade[0]["valueMulti"]
    return {
        "loot": loot['name'],
        "rarityName": rarityGrade[0]['rarity'],
        "value": value
    }
    
def print_result():
    getLoot = generate_loot()
    return f"Congratulation! You got a {getLoot['rarityName']} {getLoot['loot']}. It's worth {getLoot['value']} gold!"
    
print(print_result())
    
