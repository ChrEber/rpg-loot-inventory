import tkinter
from tkinter import ttk
import os
from PIL import Image, ImageTk

def make_background_transparent(img, bg_color_to_remove=(0, 0, 0)):
    """
    Macht eine bestimmte Farbe im Bild transparent.
    bg_color_to_remove: (0,0,0) für Schwarz oder (255,255,255) für Weiß
    """
    img = img.convert("RGBA")
    datas = img.getdata()

    new_data = []
    for item in datas:
        # Toleranz-Abgleich: Prüft ob der Pixel der zu entfernenden Farbe nahe kommt
        # (item[0]=R, item[1]=G, item[2]=B)
        if abs(item[0] - bg_color_to_remove[0]) < 30 and \
           abs(item[1] - bg_color_to_remove[1]) < 30 and \
           abs(item[2] - bg_color_to_remove[2]) < 30:
            new_data.append((255, 255, 255, 0))  # Macht den Pixel komplett transparent
        else:
            new_data.append(item)

    img.putdata(new_data)
    return img

def create_combined_icon(icon_path, bg_color, size=(32, 32)):
    # 1. Das farbige Rarity-Quadrat
    rarity_box = Image.new("RGBA", size, bg_color)
    
    if os.path.exists(icon_path):
        icon_img = Image.open(icon_path)
        
        # 2. HINTERGRUND ENTFERNEN:
        # Ändere (0,0,0) zu (255,255,255), falls dein Bild einen WEISSEN Hintergrund hat!
        icon_img = make_background_transparent(icon_img, bg_color_to_remove=(255,255,255))
        
        icon_img = icon_img.resize(size, Image.Resampling.LANCZOS)
    else:
        icon_img = Image.new("RGBA", size, (0, 0, 0, 0))

    # 3. Transparentes Icon über die Rarity-Box legen
    combined_img = Image.alpha_composite(rarity_box, icon_img)
    
    return ImageTk.PhotoImage(combined_img)


# --- TKINTER GUI TEST ---
root = tkinter.Tk()
root.title("Icon-Test mit dynamischem Hintergrund")
root.geometry("400x250")
root.configure(bg="black")

# Pfad zu deinem Icon
icon_path = os.path.join('assets', 'Allgemeines Icon.png')

# Referenzen-Speicher gegen Garbage Collection
image_references = []

def change_color(color_code):
    """Ändert das Label-Bild dynamisch auf eine neue Hintergrundfarbe."""
    # Neues zusammengesetztes Bild erstellen (z.B. 48x48 Pixel groß)
    new_icon = create_combined_icon(icon_path, color_code, size=(32, 32))
    
    # Label aktualisieren
    test_label.config(image=new_icon)
    test_label.image = new_icon # Referenz behalten!


# 1. Label für die Bildausgabe (mit bg='black', um jegliche Ränder unsichtbar zu machen)
test_label = tkinter.Label(root, bg="black", bd=0, highlightthickness=0)
test_label.pack(pady=0)

# Startbild laden (Standardmäßig Violett)
initial_icon = create_combined_icon(icon_path, "#A335EE", size=(32, 32))
test_label.config(image=initial_icon)
test_label.image = initial_icon


# 2. Test-Buttons zum dynamischen Ändern der Farbe
button_frame = tkinter.Frame(root, bg="black")
button_frame.pack()

btn_purple = tkinter.Button(
    button_frame, text="Purple (Epic)", 
    command=lambda: change_color("#A335EE")
)
btn_purple.pack(side="left", padx=5)

btn_green = tkinter.Button(
    button_frame, text="Green (Uncommon)", 
    command=lambda: change_color("#1EFF00")
)
btn_green.pack(side="left", padx=5)

btn_gold = tkinter.Button(
    button_frame, text="Gold (Legendary)", 
    command=lambda: change_color("#FF8000")
)
btn_gold.pack(side="left", padx=5)


root.mainloop()