import random

class Location:
    def __init__(self, name, item, max_items, difficulty):
        self.name = name
        self.item = item 
        self.max_items = max_items 
        self.difficulty = difficulty
    
sllpatch = Location("Small Life Leaf Patch", "Life Leaf", 2, 8)
shgpatch = Location("Small Healing Grass Patch", "Healing Grass", 4, 6)
mllpatch = Location("Medium Life Leaf Patch", "Life Leaf", 4, 8)
srhpatch = Location("Small Red Herb Patch", "Red Herb", 2, 10)