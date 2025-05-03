import random

# Parent
class Location:
    def __init__(self, name, item, max_items, difficulty):
        self.name = name
        self.item = item 
        self.max_items = max_items 
        self.difficulty = difficulty

# Material Location        
class Material(Location):
    def __init__(self, name, item, max_items, difficulty):
        super().__init__(name, item, max_items, difficulty)

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

# Only for Rocks    
class Rock(Location):
    def __init__(self, name, item, max_items, difficulty):
        super().__init__(name, item, max_items, difficulty)
        
    def rock_result(self, bonus):
        roll = random.choice(range(1, 21))
        print(roll)
        num_gathered = roll + bonus
        if num_gathered > self.max_items:
            return self.max_items
        else:
            return num_gathered

# Herbalism Locations
shgpatch = Material("Small Healing Grass Patch", "Healing Grass", 4, 6)
mhgpatch = Material("Medium Healing Grass Patch", "Healing Grass", 10, 6)
lhgpatch = Material("Large Healing Grass Patch", "Healing Grass", 20, 6)
sllpatch = Material("Small Life Leaf Patch", "Life Leaf", 2, 8)
mllpatch = Material("Medium Life Leaf Patch", "Life Leaf", 4, 8)
srhpatch = Material("Small Red Herb Patch", "Red Herb", 2, 10)
mrhpatch = Material("Medium Red Herb Patch", "Red Herb", 4, 10)
sgmpatch = Material("Small Green Moss Patch", "Green Moss", 2, 10)
sbhpatch = Material("Small Blue Herb Patch", "Blue Herb", 2, 12)
sgmrpatch = Material("Small Green Mushroom Patch", "Green Mushroom", 2, 12)

# Mining Locations
mrock = Rock("Medium Rock", "Stone", 10, 1)
lrock = Rock("Large Rock", "Stone", 20, 1)
sgmov = Material("Small Goblin Metal Ore Vein", "Goblin Metal Ore", 4, 6)
sciov = Material("Small Crude Iron Ore Vein", "Crude Iron Ore", 4, 6)
siov = Material("Small Iron Ore Vein", "Iron Ore", 4, 8)
miov = Material("Medium Iron Ore Vein", "Iron Ore", 10, 8)

class Combatant:
    def __init__(self, name, dice, num_change):
        self.name = name
        self.dice = dice
        self.num_change = num_change

    def enemy_result(self):
        roll = random.choice(range(1, self.dice + 1))
        enemy_num = roll + self.num_change
        return enemy_num
    

gsparty = Combatant("Goblin Hunting Party", 4, 2)

        