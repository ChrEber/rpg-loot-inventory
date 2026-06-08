from json_helper import JsonHelperClass

class InventoryManager:

    def __init__(self):
        self.inventory = []
        self.helper = JsonHelperClass("inventory.json")
        self.loadInventory()

    def addItem(self, item):
        self.inventory.append(item)
        if len(self.inventory) > 3:
            self.inventory.pop(0)
        self.saveInventory()

    def loadInventory(self):
        self.inventory = self.helper.load_json()
        return self.inventory

    def saveInventory(self):
        self.helper.save_json(self.inventory)

    def printInventory(self):
        if not self.inventory:
            return "Dein Inventar ist leer"
        
        lootLine = []
        for item in self.inventory:
            lootLine.append(f"{item['rarityName']} | {item['loot']} worth | {item['value']} gold")
        return "\n".join(lootLine)