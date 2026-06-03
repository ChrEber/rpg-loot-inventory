import json

inventory = []

def addItem(item):    
    inventory.append(item)
    if len(inventory) > 3:
        inventory.pop(0)

def getInventory():
    return inventory

def saveInventory(inventory):
    with open(inventory, 'w') as f:
        for item in inventory:
            f.write(f"{item['rarityName']} {item['loot']} worth {item['value']} gold\n")

def printInventory():
    for item in inventory:
        print(f"{item['rarityName']} | {item['loot']} worth | {item['value']} gold")   