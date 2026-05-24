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

valueMulti = 0

itemRarity = ["Common", "Uncommen", "Rare", "Epic", "Legendary"]
itemrarityValue = [0.9, 0.6, 0.3, 0.1, 0.01]
rarity = random.choices(itemRarity, weights = itemrarityValue, k = 1)

if rarity[0] == "Common":
    valueMulti = 0.5
elif rarity[0] == "Uncommen":
    valueMulti = 1
elif rarity[0] == "Rare":
    valueMulti = 3
elif rarity[0] == "Epic":
    valueMulti = 5
elif rarity[0] == "Legendary":
    valueMulti = 10

# match rarity[0]:
#    case "Common":
#      valueMulti = 0,5
#    case "Uncommen":
#      valueMulti = 1
#    case "Rare":
#      valueMulti = 3
#    case "Epic":
#      valueMulti = 5
#    case "Legendary":
#      valueMulti = 10

value = 0.0    
value = loot["baseValue"] * valueMulti
    
print(f"Congratulation! You got a {rarity[0]} {loot["name"]}. It's worth {value} gold!")
