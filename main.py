import json
import random

with open('items.json','r') as file:
  obj = json.load(file)
  
loot = random.choice(obj)
    
print(f"Congratulation! You got a {loot["rarity"]} {loot["name"]}. It's worth {loot["value"]} gold!")
