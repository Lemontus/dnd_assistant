import random

# Parent
class Location:
    def __init__(self, name, item, max_items, difficulty):
        self.name = name
        self.item = item 
        self.max_items = max_items 
        self.difficulty = difficulty

# Material Location        
class Vein(Location):
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

# Only for Rocks Location
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

# Groups of enemies
class Combatant:
    def __init__(self, name, dice, num_change):
        self.name = name
        self.dice = dice
        self.num_change = num_change

    def enemy_result(self):
        roll = random.choice(range(1, self.dice + 1))
        enemy_num = roll + self.num_change
        return enemy_num

# Class for items
class Item:
    def __init__(self, name, description, difficulty, id=0):
        self.name = name
        self.description = description
        self.difficulty = difficulty
        self.id = id

# Class for potions
class Potion(Item):
    def __init__(self, name, description, difficulty, ingr1, ingr2, ingr3, ingr4, ingr5, key):
        super().__init__(name, description, difficulty)
        self.ingr1 = ingr1
        self.ingr2 = ingr2
        self.ingr3 = ingr3
        self.ingr4 = ingr4
        self.ingr5 = ingr5
        self.key = key

    def brew_potion(self, bonus=0):
        roll = random.choice(range(1, 21))
        craft_roll = roll + bonus
        print(craft_roll)
        if craft_roll >= self.difficulty:
            return f"You succesfully brewed {self.description}"
        else:
            return "You failed to brew anything"

# Herbs
hgrass = Item("Healing Grass", "", 6, 0)
lleaf = Item("Life Leaf", "", 8, 1)
rherb = Item("Red Herb", "", 10, 2)
bherb = Item("Blue Herb", "", 12, 3)
blherb = Item("Black Herb", "", 20, 4)
gmoss = Item("Green Moss", "", 10, 5)
ymoss = Item("Yellow Moss", "", 12, 6)
pmoss = Item("Purple Moss", "", 15, 7)
vmoss = Item("Violet Moss", "", 20, 8)
gshroom = Item("Green Mushroom", "", 12, 9)
rshroom = Item("Red Mushroom", "", 14, 10)
bshroom = Item("Blue Mushroom", "", 16, 11)
pshroom = Item("Purple Mushroom", "", 16, 12)

# Metal
stone = Item("Stone", "", 1, 13)
gmore = Item("Goblin Metal Ore", "", 6, 14)
ciore = Item("Crude Iron Ore", "", 6, 15)
iore = Item("Iron Ore", "", 8, 16)
coal = Item("Coal", "", 12, 17)
diore = Item("Dark Iron Ore", "", 14, 18)
biore = Item("Blue Iron Ore", "", 14, 19)
nore = Item("Nathrite Ore", "", 18, 20)

# Others
gbtusk = Item("Ground Boar Tusk", "", 8, 21)
lrpowder = Item("Light Red Powder", "", 14, 22)

# Special
ecpowder = Item("???", "", 20, 99)

# Potions
hwater = Potion("Healing Water", "a bottle of green watery liquid", 8, hgrass.name, hgrass.name, hgrass.name, hgrass.name, hgrass.name, f"{hgrass.id}{hgrass.id}{hgrass.id}{hgrass.id}{hgrass.id}")
lhpotion1 = Potion("Lesser Healing Potion", "a bottle of slightly red liquid", 10, lleaf.name, lleaf.name, lleaf.name, lleaf.name, lleaf.name, f"{lleaf.id}{lleaf.id}{lleaf.id}{lleaf.id}{lleaf.id}")
lhpotion2 = Potion("Lesser Healing Potion", "a bottle of slightly red liquid", 10, lleaf.name, lleaf.name, lleaf.name, lleaf.name, rherb.name, f"{lleaf.id}{lleaf.id}{lleaf.id}{lleaf.id}{rherb.id}")
lhpotion3 = Potion("Lesser Healing Potion", "a bottle of slightly red liquid", 10, lleaf.name, lleaf.name, lleaf.name, lleaf.name, gmoss.name, f"{lleaf.id}{lleaf.id}{lleaf.id}{lleaf.id}{gmoss.id}")
lhpotion4 = Potion("Lesser Healing Potion", "2 bottles of slightly red liquid", 10, gmoss.name, gmoss.name, gmoss.name, gmoss.name, gmoss.name, f"{gmoss.id}{gmoss.id}{gmoss.id}{gmoss.id}{gmoss.id}")
hpotion = Potion("Healing Potion", "a bottle of red liquid", 12, lleaf.name, lleaf.name, lleaf.name, rherb.name, rherb.name, f"{lleaf.id}{lleaf.id}{lleaf.id}{rherb.id}{rherb.id}")
phpotion = Potion("Potent Healing Potion", "a bottle of bright red liquid", 14, lleaf.name, lleaf.name, lleaf.name, rherb.name, rshroom.name, f"{lleaf.id}{lleaf.id}{lleaf.id}{rherb.id}{rshroom.id}")
ghpotion = Potion("Greater Healing Potion", "a bottle of thick bright red liquid", 16, lleaf.name, lleaf.name, rshroom.name, rshroom.name, ymoss.name, f"{lleaf.id}{lleaf.id}{ymoss.id}{rshroom.id}{rshroom.id}")
frpotion = Potion("Frost Resistance Potion", "a bottle of bright blue liquid with a minty scent", 16, lleaf.name, bherb.name, bherb.name, bshroom.name, bshroom.name, f"{lleaf.id}{bherb.id}{bherb.id}{bshroom.id}{bshroom.id}")
lantidote = Potion("Lesser Antidote", "a bottle of light green liquid", 12, lleaf.name, lleaf.name, lleaf.name, lleaf.name, bherb.name, f"{lleaf.id}{lleaf.id}{lleaf.id}{lleaf.id}{bherb.id}")
ppoison = Potion("Potent Poison", "a bottle of dark purple liquid", 14, bherb.name, bherb.name, rherb.name, rherb.name, rherb.name, f"{rherb.id}{rherb.id}{rherb.id}{bherb.id}{bherb.id}")
prpotion = Potion("Purple Rejuvenating Potion", "a bottle of thick bright purple liquid", 18, vmoss.name, vmoss.name, pshroom.name, pshroom.name, ecpowder.name, f"{vmoss.id}{vmoss.id}{pshroom.id}{pshroom.id}{ecpowder.id}")
lspotion = Potion("Long Strider Potion", "a bottle of light yellow liquid", 10, lleaf.name, lleaf.name, lleaf.name, gbtusk.name, gbtusk.name, f"{lleaf.id}{lleaf.id}{lleaf.id}{gbtusk.id}{gbtusk.id}")
rcreagent = Potion("Rust Cleaning Reagent", "a bottle of gray liquid", 14, rherb.name, rherb.name, rherb.name, lrpowder.name, lrpowder.name, f"{rherb.id}{rherb.id}{rherb.id}{lrpowder.id}{lrpowder.id}")

# Herbalism Locations
shgpatch = Vein("Small Healing Grass Patch", hgrass.name, 4, hgrass.difficulty)
mhgpatch = Vein("Medium Healing Grass Patch", hgrass.name, 10, hgrass.difficulty)
lhgpatch = Vein("Large Healing Grass Patch", hgrass.name, 20, hgrass.difficulty)
sllpatch = Vein("Small Life Leaf Patch", lleaf.name, 2, lleaf.difficulty)
mllpatch = Vein("Medium Life Leaf Patch", lleaf.name, 4, lleaf.difficulty)
srhpatch = Vein("Small Red Herb Patch", rherb.name, 2, rherb.difficulty)
mrhpatch = Vein("Medium Red Herb Patch", rherb.name, 4, rherb.difficulty)
sgmpatch = Vein("Small Green Moss Patch", gmoss.name, 2, gmoss.difficulty)
sbhpatch = Vein("Small Blue Herb Patch", bherb.name, 2, bherb.difficulty)
sgmrpatch = Vein("Small Green Mushroom Patch", gshroom.name, 2, gshroom.difficulty)

# Mining Locations
mrock = Rock("Medium Rock", stone.name, 10, stone.difficulty)
lrock = Rock("Large Rock", stone.name, 20, stone.difficulty)
sgmov = Vein("Small Goblin Metal Ore Vein", gmore.name, 4, gmore.difficulty)
mgmov = Vein("Medium Goblin Metal Ore Vein", gmore.name, 10, gmore.difficulty)
lgmov = Vein("Large Goblin Metal Ore Vein", gmore.name, 20, gmore.difficulty)
sciov = Vein("Small Crude Iron Ore Vein", ciore.name, 4, ciore.difficulty)
siov = Vein("Small Iron Ore Vein", iore.name, 4, iore.difficulty)
miov = Vein("Medium Iron Ore Vein", iore.name, 10, iore.difficulty)
snov = Vein("Small Nathrite Ore Vein", nore.name, 2, nore.difficulty)
scv = Vein("Small Coal Vein", coal.difficulty, 4, coal.difficulty)
sdiov = Vein("Small Dark Iron Ore Vein", diore.name, 4, diore.difficulty)

# Monster groups
gsparty = Combatant("Goblin Hunting Party", 4, 2)
bparty = Combatant("Bandit Party", 4, 0)

        