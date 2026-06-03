# itemclass:
# 0 = misc
# 1 = weapon
# 2 = armor
# 3 = consumables
# 4 = materials
from data import generate_loot
from inventory import addItem, printInventory
def main():
    loot = generate_loot()
    addItem(loot)

    print(f"Congratulation!\n You got a {loot['rarityName']} {loot['loot']}.\n It's worth {loot['value']} gold!")
    print("--------------------------------------------------")
    printInventory()
    print("--------------------------------------------------")
main()