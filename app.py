import tkinter
import data
import os
from inventory import InventoryManager

inventory_manager = InventoryManager()
inventory_frame = None
outputInventory = None

def update_inventory_display():
    if inventory_frame is not None and inventory_frame.winfo_exists() and outputInventory is not None:
        outputInventory.config(state='normal')
        outputInventory.delete('1.0', tkinter.END)
        outputInventory.image_labels = []

        for item in inventory_manager.inventory:
            farbe = item['rarityColor']
            
            icon_label = tkinter.Label(
                outputInventory, 
                image=loot_image, 
                bg=farbe, 
                borderwidth=0, 
                highlightthickness=0,
                padx=0,
                pady=0
            )
            icon_label.image = loot_image
            outputInventory.image_labels.append(icon_label)

            outputInventory.window_create(
                tkinter.END, 
                window=icon_label, 
                align="center", 
                padx=0, 
                pady=0
            )
            
            text_zeile = f"  {item['loot']} | Wert: {item['value']} Gold\n\n"
            outputInventory.tag_config(farbe, foreground=farbe)
            outputInventory.insert(tkinter.END, text_zeile, farbe)
            
        outputInventory.config(state='disabled')

def roll_button():
    loot = data.generate_loot()
    inventory_manager.addItem(loot)
    outputText.config(image=loot_image, text="", bg=loot["rarityColor"])
        #outputText.config(text=f"Congratulation!\n You got a {loot['rarityName']} {loot['loot']}.\n It's worth {loot['value']} gold!", bg=loot["rarityColor"])
    outputText.image = loot_image

    update_inventory_display()

def show_inventory():
    global inventory_frame, outputInventory

    if inventory_frame is not None and inventory_frame.winfo_exists():
     inventory_frame.destroy()
     inventory_frame = None
     outputInventory = None
     return
    
    inventory_frame = tkinter.Frame(root, bg = 'black', width=400, height=200)
    inventory_frame.pack(side='right', fill='both', expand=False, padx= 15, pady=15)

    outputInventory = tkinter.Text(inventory_frame, bg='black', font=('Arial', 10, 'bold'), borderwidth=0, highlightthickness=0, width=35, height=1)
    outputInventory.pack(expand=True, fill='both')

    update_inventory_display()

root = tkinter.Tk()

items_bild = os.path.join('assets', 'Allgemeines Icon.png')
loot_image = tkinter.PhotoImage(file=items_bild)

root.title('RPG Loot Generator')
root.configure(background = 'black')
root.eval('tk::PlaceWindow . center')
root.resizable(width=True, height=False)

loot_kiste = tkinter.Frame(root, bg = 'black', width=200, height=200)
loot_kiste.pack_propagate(False)
loot_kiste.pack(side='left', fill='both', expand=True)

outputText = tkinter.Label(loot_kiste, text="Öffne die Kiste!\n Seh wieviel Glück du hast.")
outputText.pack(expand=True)

outputButton = tkinter.Button(loot_kiste, text="Öffne die Lootbox", command=roll_button)
outputButton.pack(expand=True)

outputButton2 = tkinter.Button(loot_kiste, text="Zeige das Inventar", command=show_inventory)
outputButton2.pack(expand=True)

root.mainloop()
