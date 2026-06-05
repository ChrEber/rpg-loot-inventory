# itemclass:
# 0 = misc
# 1 = weapon
# 2 = armor
# 3 = consumables
# 4 = materials
from inventory import InventoryManager
from data import generate_loot

def main():
    loot = generate_loot()
    inventory_manager = InventoryManager()
    inventory_manager.addItem(loot)

    print(f"Congratulation!\n You got a {loot['rarityName']} {loot['loot']}.\n It's worth {loot['value']} gold!")
    print("--------------------------------------------------")
    inventory_manager.printInventory()
    print("--------------------------------------------------")
main()