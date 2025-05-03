import locations
import random
from locations import *

def plains(dice, bonus):
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
        gathered = int(shgpatch.gather_result(bonus))
        item = shgpatch.item
    elif dice > 95 and dice <= 100:
        patch = sllpatch.name #Small Life Leaf
        gathered = int(sllpatch.gather_result(bonus))
        item = sllpatch.item

    if patch == "Nothing":
        return "You failed to find anything!"
    else:
        return f"You found {patch}! and gathered {gathered} of {item}!"