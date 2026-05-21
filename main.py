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
    
print(f"Congratulation! You got a {loot["rarity"]} {loot["name"]}. It's worth {loot["value"]} gold!")
