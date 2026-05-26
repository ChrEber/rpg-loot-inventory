import json
import random

def load_items():
    with open("items.json", "r") as file:
        items = json.load(file)
    return items


def roll_loot():
    item = load_items()
    loot = random.choice(item)
    return loot
