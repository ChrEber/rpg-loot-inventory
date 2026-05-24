# itemclass:
# 0 = misc
# 1 = weapon
# 2 = armor
# 3 = consumables
# 4 = materials

import json
import random

with open('items.json','r') as file:
  obj = json.load(file)
  
loot = random.choice(obj)

rarityKeys = ['id', 'rarity', 'itemRarityValue', 'valueMulti', 'rarityColor']

itemRarity_Liste = {}
itemRarity_Liste = [
	[0, "Common",    90, 0.5, "#ffffff"],
	[1, "Uncommon",  60,   1, "#00ff00"],
	[2, "Rare",      30,   3, "#0080ff"],
	[3, "Epic",      10,   5, "#a020f0"],
	[4, "Legendary",  1,  10, "#ff9900"]
]

itemRarity_Dict = [dict(zip(rarityKeys, datensatz)) for datensatz in itemRarity_Liste]

gewichtung = []
for i in range(len(itemRarity_Dict)):
    gewichtung.append(itemRarity_Dict[i]["itemRarityValue"])

rarity = random.choices(itemRarity_Dict, weights = gewichtung, k = 1)

value = 0    
value = loot['baseValue'] * rarity[0]["valueMulti"]
    
print(f"Congratulation! You got a {rarity[0]["rarity"]} {loot['name']}. It's worth {value} gold!")
