import random

class Location:
    def __init__(self, name, item, max_items, difficulty):
        self.name = name
        self.item = item 
        self.max_items = max_items 
        self.difficulty = difficulty

    def gather_result(self, bonus):
        roll = random.choice(range(1, 21))
        print(roll)
        gather_roll = roll + bonus
        num_gathered = 0
        while gather_roll >= self.difficulty:
            num_gathered += 1
            gather_roll -= 2
        
        if num_gathered > self.max_items:
            return self.max_items
        else:
            return num_gathered
    
shgpatch = Location("Small Healing Grass Patch", "Healing Grass", 4, 6)
mhgpatch = Location("Medium Healing Grass Patch", "Healing Grass", 10, 6)
lhgpatch = Location("Large Healing Grass Patch", "Healing Grass", 20, 6)
sllpatch = Location("Small Life Leaf Patch", "Life Leaf", 2, 8)
mllpatch = Location("Medium Life Leaf Patch", "Life Leaf", 4, 8)
srhpatch = Location("Small Red Herb Patch", "Red Herb", 2, 10)
mrhpatch = Location("Medium Red Herb Patch", "Red Herb", 4, 10)
sgmpatch = Location("Small Green Moss Patch", "Green Moss", 2, 10)
sbhpatch = Location("Small Blue Herb Patch", "Blue Herb", 2, 12)
sgmrpatch = Location("Small Green Mushroom Patch", "Green Mushroom", 2, 12)

