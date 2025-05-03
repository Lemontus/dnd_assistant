import class_lib
import random
from class_lib import *

def forest_hunt():
    roll = random.choice(range(1, 11))
    monster = ["Arzuros", "Bulldrome", "Lagombi", "Buldrome", "Buldrome", "Buldrome", "Lagombi", "Lagombi", "Zinogre", "Arzuros"]
    i = roll - 1
    return monster[i]



# Roll functions for the plains region
def plains_herb(dice, bonus):
    if dice <= 8:
        patch = sllpatch.name #Small Life Leaf
        gathered = sllpatch.gather_result(bonus)
        item = sllpatch.item
    elif dice > 8 and dice <= 32:
        patch = "Nothing"
    elif dice > 32 and dice <= 37:
        patch = sllpatch.name #Small Life Leaf
        gathered = sllpatch.gather_result(bonus)
        item = sllpatch.item
    elif dice > 37 and dice <= 63:
        patch = shgpatch.name #Small Healing Grass
        gathered = shgpatch.gather_result(bonus)
        item = shgpatch.item
    elif dice > 63 and dice <= 67:
        patch = mllpatch.name #Medium Life Leaf
        gathered = mllpatch.gather_result(bonus)
        item = mllpatch.item
    elif dice > 67 and dice <= 72:
        patch = srhpatch.name #Small Red Herb
        gathered = srhpatch.gather_result(bonus)
        item = srhpatch.item
    elif dice > 72 and dice <= 95:
        patch = shgpatch.name #Small Healing Grass
        gathered = shgpatch.gather_result(bonus)
        item = shgpatch.item
    elif dice > 95 and dice <= 100:
        patch = sllpatch.name #Small Life Leaf
        gathered = sllpatch.gather_result(bonus)
        item = sllpatch.item

    if patch == "Nothing":
        return "You failed to find anything!"
    else:
        return f"You found {patch}! and gathered {gathered} of {item}!"
    
# Roll function for the Great Forest region
def forest_herb(dice, bonus):

    combat = False
    hunt = False

    if dice <= 5:
        patch = sgmpatch.name #Small Green Moss
        gathered = sgmpatch.gather_result(bonus)
        item = sgmpatch.item
    elif dice > 5 and dice <= 11:
        patch = shgpatch.name #Small Healing Grass
        gathered = shgpatch.gather_result(bonus)
        item = shgpatch.item
    elif dice > 11 and dice <= 13:
        hunt = True
        monster = forest_hunt()
    elif dice > 13 and dice <= 17:
        patch = sbhpatch.name #Small Blue Herb
        gathered = sbhpatch.gather_result(bonus)
        item = sbhpatch.item
    elif dice > 17 and dice <= 20:
        patch = mrhpatch.name #Medium Red Herb
        gathered = mrhpatch.gather_result(bonus)
        item = mrhpatch.item
    elif dice > 20 and dice <= 27:
        combat = True
        enemy = gsparty.name # Goblin Scouting Party
        enemy_num = gsparty.enemy_result()
    elif dice > 27 and dice <= 32:
        patch = sllpatch.name #Small Life Leaf
        gathered = sllpatch.gather_result(bonus)
        item = sllpatch.item
    elif dice > 32 and dice <= 37:
        patch = mllpatch.name #Medium Life leaf
        gathered = mllpatch.gather_result(bonus)
        item = mllpatch.item
    elif dice > 37 and dice <= 41:
        patch = sgmrpatch.name #Small Green Mushroom
        gathered = sgmrpatch.gather_result(bonus)
        item = sgmrpatch.item
    elif dice > 41 and dice <= 46:
        patch = mllpatch.name #Medium Life leaf
        gathered = mllpatch.gather_result(bonus)
        item = mllpatch.item
    elif dice > 46 and dice <= 57:
        patch = mhgpatch.name #Medium Healing Grass
        gathered = mhgpatch.gather_result(bonus)
        item = mhgpatch.item
    elif dice > 57 and dice <= 63:
        patch = shgpatch.name #Small Healing Grass
        gathered = shgpatch.gather_result(bonus)
        item = shgpatch.item
    elif dice > 63 and dice <= 70:
        patch = sllpatch.name #Small Life Leaf
        gathered = sllpatch.gather_result(bonus)
        item = sllpatch.item
    elif dice > 70 and dice <= 76:
        combat = True
        enemy = gsparty.name # Goblin Scouting Party
        enemy_num = gsparty.enemy_result()
    elif dice > 76 and dice <= 82:
        patch = lhgpatch.name #Large Healing Grass
        gathered = lhgpatch.gather_result(bonus)
        item = lhgpatch.item
    elif dice > 82 and dice <= 88:
        patch = srhpatch.name #Small Red Herb
        gathered = srhpatch.gather_result(bonus)
        item = srhpatch.item
    elif dice > 88 and dice <= 94:
        patch = shgpatch.name #Small Healing Grass
        gathered = shgpatch.gather_result(bonus)
        item = shgpatch.item
    elif dice > 94 and dice <= 100:
        patch = sllpatch.name #Small Life Leaf
        gathered = sllpatch.gather_result(bonus)
        item = sllpatch.item

    if combat == True:
        return f"You have stumbled upon a {enemy} with {enemy_num} enemies"
    elif hunt == True:
        return f"You were unlucky enough to encounter {monster}"
    else:
        return f"You found {patch}! and gathered {gathered} of {item}!"