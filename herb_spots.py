import locations
import random
from locations import *

def plains(dice):
    if dice <= 8:
        location = sllpatch.name #Small Life Leaf
    elif dice > 8 and dice <= 32:
        location = "Nothing"
    elif dice > 32 and dice <= 37:
        location = sllpatch.name #Small Life Leaf
    elif dice > 37 and dice <= 63:
        location = shgpatch.name #Small Healing Grass
    elif dice > 63 and dice <= 67:
        location = mllpatch.name #Medium Life Leaf
    elif dice > 67 and dice <= 72:
        location = srhpatch.name #Small Red Herb
    elif dice > 72 and dice <= 95:
        location = shgpatch.name #Small Healing Grass
    elif dice > 95 and dice <= 100:
        location = sllpatch.name #Small Life Leaf
    return location