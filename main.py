import json
import random

# itemclass:
# 0 = misc
# 1 = weapon
# 2 = armor
# 3 = consumables
# 4 = materials

with open('items.json','r') as file:
  obj = json.load(file)
  
loot = random.choice(obj)

itemRarity = ["Common", "Uncommen", "Rare", "Epic", "Legendary"]

rarity = ""
rarity = random.choice(itemRarity)

valueMulti = 0

if rarity == "Common":
    valueMulti = 0.5
elif rarity == "Uncommen":
    valueMulti = 1
elif rarity == "Rare":
    valueMulti = 3
elif rarity == "Epic":
    valueMulti = 5
elif rarity == "Legendary":
    valueMulti = 10

value = 0.0    
value = loot["baseValue"] * valueMulti
    
print(f"Congratulation! You got a {rarity} {loot["name"]}. It's worth {value} gold!")
