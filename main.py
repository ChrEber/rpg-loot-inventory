import json

with open('items.json','r') as file:
  obj = json.load(file)

print(obj[0]["name"])
