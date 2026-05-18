import json
import random

with open('items.json','r') as file:
  obj = json.load(file)
  
loot = random.choice(obj)
    
print(loot["name"])
