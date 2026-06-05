import tkinter
import data
from inventory import InventoryManager

inventory_manager = InventoryManager()

root = tkinter.Tk()
root.title('RPG Loot Generator')
root.configure(background = 'black')
root.minsize(200, 200)
root.maxsize(500, 500)
root.eval('tk::PlaceWindow . center')

def roll_button():
    loot = data.generate_loot()
    inventory_manager.addItem(loot)
    outputText.config(text=f"Congratulation!\n You got a {loot['rarityName']} {loot['loot']}.\n It's worth {loot['value']} gold!", bg=loot["rarityColor"])

def show_inventory():
    inventory_manager.printInventory()

outputText = tkinter.Label(root, text="Öffne die Kiste!\n Seh wieviel Glück du hast.")
outputText.pack(expand=True)

outputButton = tkinter.Button(root, text="Öffne die Lootbox", command=roll_button)
outputButton.pack(expand=True)

root.mainloop()
