from loot import roll_loot
from rarity import roll_rarity

def generate_loot():
    value = 0
    loot = roll_loot()
    rarityGrade = roll_rarity()
    value = loot["baseValue"] * rarityGrade[0]["valueMulti"]
    return {
        "loot": loot["name"],
        "rarityName": rarityGrade[0]["rarity"],
        "value": value,
    }


def print_result():
    getLoot = generate_loot()
    return f"Congratulation! You got a {getLoot['rarityName']} {getLoot['loot']}. It's worth {getLoot['value']} gold!"
