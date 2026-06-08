import tkinter
import data
from inventory import InventoryManager

inventory_manager = InventoryManager()

inventoryWindow = None
outputInventory = None


root = tkinter.Tk()
root.title('RPG Loot Generator')
root.configure(background = 'black')
root.minsize(200, 200)
root.maxsize(500, 500)
root.eval('tk::PlaceWindow . center')

def update_inventory_display():
    if inventoryWindow is not None and inventoryWindow.winfo_exists() and outputInventory is not None:
        outputInventory.config(state='normal')
        outputInventory.delete('1.0', tkinter.END)
        for item in inventory_manager.inventory:
            text_zeile = f"{item['rarityName']} | {item['loot']} | Wert: {item['value']} Gold\n"
            farbe = item['rarityColor']
            outputInventory.tag_config(farbe, foreground=farbe)
            outputInventory.insert(tkinter.END, text_zeile, farbe)
        outputInventory.config(state='disabled')

def roll_button():
    global outputInventory

    loot = data.generate_loot()
    inventory_manager.addItem(loot)
    outputText.config(text=f"Congratulation!\n You got a {loot['rarityName']} {loot['loot']}.\n It's worth {loot['value']} gold!", bg=loot["rarityColor"])

    update_inventory_display()

def show_inventory():
    global inventoryWindow, outputInventory

    if inventoryWindow is not None and inventoryWindow.winfo_exists():
        inventoryWindow.destroy()
        inventoryWindow = None
        outputInventory = None
        return

    inventoryWindow = tkinter.Toplevel(root)
    inventoryWindow.title('Inventory')
    inventoryWindow.configure(background = 'black')
    inventoryWindow.minsize(300, 300)
    inventoryWindow.maxsize(600, 600)
    inventoryWindow.eval('tk::PlaceWindow . center')

    outputInventory = tkinter.Text(inventoryWindow, bg='black', font=('Arial', 10, 'bold'), borderwidth=0, highlightthickness=0)
    outputInventory.pack(expand=True, fill='both', padx=20, pady=20)

outputText = tkinter.Label(root, text="Öffne die Kiste!\n Seh wieviel Glück du hast.")
outputText.pack(expand=True)

outputButton = tkinter.Button(root, text="Öffne die Lootbox", command=roll_button)
outputButton.pack(expand=True)

outputButton2 = tkinter.Button(root, text="Zeige das Inventar", command=show_inventory)
outputButton2.pack(expand=True)

root.mainloop()
