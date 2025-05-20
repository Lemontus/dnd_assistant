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
        gather_roll = roll + bonus
        print(f"Roll:{roll} Bonus: {bonus}")
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
        print(roll, bonus)
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
        self.dic = str.lower(name)

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
        
# Class for processed materials
class Material(Item):
    def __init__(self, name, description, difficulty, id, ingr, num=1):
        super().__init__(name, description, difficulty, id)
        self.ingr = ingr
        self.num = num
        self.dic = str.lower(name)

    def process_material(self, bonus=0):
        roll = random.choice(range(1, 21))
        craft_roll = roll + bonus
        print(craft_roll)
        if craft_roll >= self.difficulty:
            return f"You succesfully processed {self.num} {self.ingr} into a {self.name}"
        else:
            return "You failed to process the materials"

# Herbs
hgrass = Item("Healing Grass", "It's grass", 6, 0)
lleaf = Item("Life Leaf", "It's green", 8, 1)
rherb = Item("Red Herb", "It's red", 10, 2)
bherb = Item("Blue Herb", "It's blue", 12, 3)
blherb = Item("Black Herb", "It's black", 20, 4)
gmoss = Item("Green Moss", "It's green but moss", 10, 5)
ymoss = Item("Yellow Moss", "It's yellow but moss", 12, 6)
pmoss = Item("Purple Moss", "It's purple but moss", 15, 7)
vmoss = Item("Violet Moss", "It's violet but moss", 20, 8)
gshroom = Item("Green Mushroom", "It's green but mushroom", 12, 9)
rshroom = Item("Red Mushroom", "It's red but mushroom", 14, 10)
bshroom = Item("Blue Mushroom", "It's blue but mushroom", 16, 11)
pshroom = Item("Purple Mushroom", "It's purple but mushroom", 16, 12)

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
btusk = Item("Boar Tusk", "", 8, 21)

lrpowder = Item("Light Red Powder", "", 14, 22)

# Processed Materials
lleafp = Material("Life Leaf Pulp", "It's green", 8, 23, lleaf.name)
dlleaf = Material("Dried Life Leaf", "It's green", 8, 24, lleaf.name)
rherbp = Material("Red Herb Pulp", "It's red", 10, 25, rherb.name)
drherb = Material("Dried Red Herb", "It's red", 10, 26, rherb.name) 
bherbp = Material("Blue Herb Pulp", "It's blue", 12, 27, bherb.name)
dbherb = Material("Dried Blue Herb", "It's blue", 12, 28, bherb.name)
blherbp = Material("Black Herb Pulp", "It's black", 20, 29, blherb.name)
dblherb = Material("Dried Black Herb", "It's black", 20, 30, blherb.name)
gmossp = Material("Green Moss Pulp", "It's green but moss", 10, 31, gmoss.name)
dgmoss = Material("Dried Green Moss", "It's green but moss", 10, 32, gmoss.name)
ymossp = Material("Yellow Moss Pulp", "It's yellow but moss", 12, 33, ymoss.name)
dymoss = Material("Dried Yellow Moss", "It's yellow but moss", 12, 34, ymoss.name)
pmossp = Material("Purple Moss Pulp", "It's purple but moss", 15, 35, pmoss.name)
dpmoss = Material("Dried Purple Moss", "It's purple but moss", 15, 36, pmoss.name)
vmossp = Material("Violet Moss Pulp", "It's violet but moss", 20, 37, vmoss.name)
dvmoss = Material("Dried Violet Moss", "It's violet but moss", 20, 38, vmoss.name)
gshroomp = Material("Green Mushroom Pulp", "It's green but mushroom", 12, 39, gshroom.name)
dgshroom = Material("Dried Green Mushroom", "It's green but mushroom", 12, 40, gshroom.name)
rshroomp = Material("Red Mushroom Pulp", "It's red but mushroom", 14, 41, rshroom.name)
drshroom = Material("Dried Red Mushroom", "It's red but mushroom", 14, 42, rshroom.name)
bshroomp = Material("Blue Mushroom Pulp", "It's blue but mushroom", 16, 43, bshroom.name)
dbshroom = Material("Dried Blue Mushroom", "It's blue but mushroom", 16, 44, bshroom.name)
pshroomp = Material("Purple Mushroom Pulp", "It's purple but mushroom", 16, 45, pshroom.name)
dpshroom = Material("Dried Purple Mushroom", "It's purple but mushroom", 16, 46, pshroom.name)
gmingot = Material("Goblin Metal Ingot", "It's a green'ish metal ingot", 6, 47, gmore.name, 8)
ciingot = Material("Crude Iron Ingot", "It's crude iron ingot", 6, 48, ciore.name, 8)
iingot = Material("Iron Ingot", "It's a regular iron ingot", 8, 49, iore.name, 8)
iingot2 = Material("Iron Ingot", "It's a regular iron ingot", 10, 50, ciore.name, 16)
dsingot = Material("Dark Steel Ingot", "It's an ingot made of durable metal with a dark tint", 14, 51, f"{diore.name} and 4 {coal.name}", 4)
bsingot = Material("Blue Steel Ingot", "It's an ingot made of durable metal with a blue tint", 14, 52, f"{biore.name} and 4 {coal.name}", 4)
ningot = Material("Nathrite Ingot", "It's an ingot made of an extremely durable metal with a purple tint", 18, 53, nore.name, 8)
gbtusk = Material("Ground Boar Tusk", "It's a ground boar tusk", 8, 54, btusk.name)

# Advanced Processed Materials
gmplate = Material("Goblin Metal Plate", "It's a plate made of Goblin Metal", 10, 55, f"2 {gmingot.name}s")
ciplate = Material("Crude Iron Plate", "It's a plate made of Crude Iron", 10, 56, f"2 {ciingot.name}s")
iplate = Material("Iron Plate", "It's a plate made of Iron", 12, 57, f"2 {iingot.name}s")
dsplate = Material("Dark Steel Plate", "It's a plate made of Dark Steel", 16, 58, f"2 {dsingot.name}s")
bsplate = Material("Blue Steel Ingot", "It's a plate made of Blue Steel", 16, 59, f"2 {bsingot.name}s")
nplate = Material("Nathrite Plate", "It's a plate made of Nathrite", 20, 60, f"2 {ningot.name}s")
gmcsheet = Material("Goblin Metal Chain Sheet", "It's a chain sheet made of Goblin Metal", 10, 61, gmingot.name)
cicsheet = Material("Crude Iron Chain Sheet", "It's a chain sheet made of Crude Iron", 10, 62, ciingot.name)
icsheet = Material("Iron Chain Sheet", "It's a chain sheet made of Regular Iron", 12, 63, iingot.name)
dscsheet = Material("Dark Steel Chain Sheet", "It's a chain sheet made of Dark Steel", 16, 64, dsingot.name)
bscsheet = Material("Blue Steel Chain Sheet", "It's a chain sheet made of Blue Steel", 16, 65, bsingot.name)
ncsheet = Material("Nathride Chain Sheet", "It's a chain sheet made of Nathrite", 20, 66, ningot.name)


# Special
ecpowder = Item("???", "", 20, 999)


# Potions
hwater = Potion("Healing Water", "a bottle of green watery liquid", 8, hgrass.name, hgrass.name, hgrass.name, hgrass.name, hgrass.name, f"{hgrass.id}{hgrass.id}{hgrass.id}{hgrass.id}{hgrass.id}")
lhpotion1 = Potion("Lesser Healing Potion", "a bottle of slightly red liquid", 10, lleafp.name, lleafp.name, lleafp.name, lleafp.name, lleafp.name, f"{lleafp.id}{lleafp.id}{lleafp.id}{lleafp.id}{lleafp.id}")
lhpotion2 = Potion("Lesser Healing Potion", "a bottle of slightly red liquid", 10, lleafp.name, lleafp.name, lleafp.name, lleafp.name, rherbp.name, f"{lleafp.id}{lleafp.id}{lleafp.id}{lleafp.id}{rherbp.id}")
lhpotion3 = Potion("Lesser Healing Potion", "a bottle of slightly red liquid", 10, lleafp.name, lleafp.name, lleafp.name, lleafp.name, gmossp.name, f"{lleafp.id}{lleafp.id}{lleafp.id}{lleafp.id}{gmossp.id}")
lhpotion4 = Potion("Lesser Healing Potion", "2 bottles of slightly red liquid", 10, gmossp.name, gmossp.name, gmossp.name, gmossp.name, gmossp.name, f"{gmossp.id}{gmossp.id}{gmossp.id}{gmossp.id}{gmossp.id}")
hpotion = Potion("Healing Potion", "a bottle of red liquid", 12, lleafp.name, lleafp.name, lleafp.name, rherbp.name, rherbp.name, f"{lleafp.id}{lleafp.id}{lleafp.id}{rherbp.id}{rherbp.id}")
phpotion = Potion("Potent Healing Potion", "a bottle of bright red liquid", 14, lleafp.name, lleafp.name, lleafp.name, rherbp.name, rshroomp.name, f"{lleafp.id}{lleafp.id}{lleafp.id}{rherbp.id}{rshroomp.id}")
ghpotion = Potion("Greater Healing Potion", "a bottle of thick bright red liquid", 16, lleafp.name, lleafp.name, rshroomp.name, rshroomp.name, ymossp.name, f"{lleafp.id}{lleafp.id}{ymossp.id}{rshroomp.id}{rshroomp.id}")
frpotion = Potion("Frost Resistance Potion", "a bottle of bright blue liquid with a minty scent", 16, lleafp.name, bherbp.name, bherbp.name, bshroomp.name, bshroomp.name, f"{lleafp.id}{bherbp.id}{bherbp.id}{bshroomp.id}{bshroomp.id}")
lantidote = Potion("Lesser Antidote", "a bottle of light green liquid", 12, lleafp.name, lleafp.name, lleafp.name, lleafp.name, bherbp.name, f"{lleafp.id}{lleafp.id}{lleafp.id}{lleafp.id}{bherbp.id}")
ppoison = Potion("Potent Poison", "a bottle of dark purple liquid", 14, bherbp.name, bherbp.name, rherbp.name, rherbp.name, rherbp.name, f"{rherbp.id}{rherbp.id}{rherbp.id}{bherbp.id}{bherbp.id}")
prpotion = Potion("Purple Rejuvenating Potion", "a bottle of thick bright purple liquid", 18, vmossp.name, vmossp.name, pshroomp.name, pshroomp.name, ecpowder.name, f"{vmossp.id}{vmossp.id}{pshroomp.id}{pshroomp.id}{ecpowder.id}")
lspotion = Potion("Long Strider Potion", "a bottle of light yellow liquid", 10, lleafp.name, lleafp.name, lleafp.name, gbtusk.name, gbtusk.name, f"{lleafp.id}{lleafp.id}{lleafp.id}{gbtusk.id}{gbtusk.id}")
rcreagent = Potion("Rust Cleaning Reagent", "a bottle of gray liquid", 14, rherbp.name, rherbp.name, rherbp.name, lrpowder.name, lrpowder.name, f"{rherbp.id}{rherbp.id}{rherbp.id}{lrpowder.id}{lrpowder.id}")

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

        