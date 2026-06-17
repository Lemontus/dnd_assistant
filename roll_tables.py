import class_lib
import random
from class_lib import *

# Roll table for Great Forest monster hunt
def forest_hunt():
    roll = random.choice(range(1, 11))
    monster = ["Arzuros", "Bulldrome", "Lagombi", "Buldrome", "Buldrome", "Buldrome", "Lagombi", "Lagombi", "Zinogre", "Arzuros"]
    i = roll - 1
    return monster[i]



# Roll function for herb gathering in the plains region
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
    
# Roll function for herb gathering in the Great Forest region
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
    
def plains_metal(dice, bonus):
    if dice < 5:
        vein = siov.name # Small Iron Ore
        gathered = siov.gather_result(bonus)
        item = siov.item
    elif dice > 5 and dice <= 11:
        vein = "Nothing"
    elif dice > 11 and dice <= 17:
        vein = mrock.name # Medium Rock
        gathered = mrock.rock_result(bonus)
        item = mrock.item
    elif dice > 17 and dice <= 43:
        vein = sgmov.name # Small Goblin Metal Ore
        gathered = sgmov.gather_result(bonus)
        item = sgmov.item
    elif dice > 43 and dice <= 47:
        vein = siov.name # Small Iron Ore
        gathered = siov.gather_result(bonus)
        item = siov.item
    elif dice > 47 and dice <= 56:
        vein = sciov.name # Small Crude Iron Ore
        gathered = sciov.gather_result(bonus)
        item = sciov.item
    elif dice > 56 and dice <= 61:
        vein = lrock.name # Large Rock
        gathered = lrock.rock_result(bonus)
        item = lrock.item
    elif dice > 61 and dice <= 87:
        vein = sgmov.name # Small Goblin Metal Ore
        gathered = sgmov.gather_result(bonus)
        item = sgmov.item
    elif dice > 87 and dice <= 92:
        vein = miov.name # Medium Iron Ore
        gathered = miov.gather_result(bonus)
        item = miov.item
    elif dice > 92 and dice <= 100:
        vein = "Nothing"

    if vein == "Nothing":
        return "You failed to find anything!"
    else:
        return f"You found {vein}! and gathered {gathered} of {item}!"
    

def forest_metal(dice, bonus):

    combat = False
    hunt = False

    if dice <= 5:
        vein = siov.name # Small Iron Ore
        gathered = siov.gather_result(bonus)
        item = siov.item
    elif dice > 5 and dice <= 11:
        vein = sgmov.name # Small Goblin Metal Ore
        gathered = sgmov.gather_result(bonus)
        item = sgmov.item
    elif dice > 11 and dice <= 13:
        vein = snov.name # Small Nathrite
        gathered = snov.gather_result(bonus)
        item = snov.item
    elif dice > 13 and dice <= 17:
        hunt = True
        monster = forest_hunt()
    elif dice > 17 and dice <= 20:
        vein = siov.name
        gathered = siov.gather_result(bonus)
        item = siov.item
    elif dice > 20 and dice <= 27:
        combat = True
        enemy = gsparty.name # Goblin Scouting Party
        enemy_num = gsparty.enemy_result()
    elif dice > 27 and dice <= 32:
        vein = siov.name
        gathered = siov.gather_result(bonus)
        item = siov.item
    elif dice > 32 and dice <= 37:
        vein = sciov.name
        gathered = sciov.gather_result(bonus)
        item = sciov.item
    elif dice > 37 and dice <= 41:
        vein = scv.name
        gathered = scv.gather_result(bonus)
        item = scv.item
    elif dice > 41 and dice <= 46:
        vein = mgmov.name
        gathered = mgmov.gather_result(bonus)
        item = mgmov.item
    elif dice > 46 and dice <= 57:
        vein = sgmov.name
        gathered = sgmov.gather_result(bonus)
        item = sgmov.item
    elif dice > 57 and dice <= 63:
        combat = True
        enemy = bparty.name # Bandit Party
        enemy_num = bparty.enemy_result()
    elif dice > 63 and dice <= 70:
        vein = miov.name
        gathered = miov.gather_result(bonus)
        item = miov.item
    elif dice > 70 and dice <= 76:
        vein = sgmov.name
        gathered = sgmov.gather_result(bonus)
        item = sgmov.item
    elif dice > 76 and dice <= 82:
        vein = sciov.name
        gathered = sciov.gather_result(bonus)
        item = sciov.item
    elif dice > 82 and dice <= 88:
        vein = sdiov.name
        gathered = sdiov.gather_result(bonus)
        item = sdiov.item
    elif dice > 88 and dice <= 94:
        vein = lgmov.name
        gathered = lgmov.gather_result(bonus)
        item = lgmov.item
    elif dice > 94 and dice <= 100:
        vein = siov.name
        gathered = siov.gather_result(bonus)
        item = siov.item

    if combat == True:
        return f"You have stumbled upon a {enemy} with {enemy_num} enemies"
    elif hunt == True:
        return f"You were unlucky enough to encounter {monster}"
    else:
        return f"You found {vein}! and gathered {gathered} of {item}!"
    
# Roll function for random kingdom events
def k_events(dice):
    if dice <= 3:
        return "Archeological Find"
    elif dice > 3 and dice <= 5:
        return "Assassination Attempt"
    elif dice > 5 and dice <= 7:
        camp_size = bcamp.enemy_result()
        print(camp_size)
        return "Bandit Activity"
    elif dice > 7 and dice <= 10:
        return "Placeholder"
    elif dice > 10 and dice <= 14:
        return "Building Demand"
    elif dice > 14 and dice <= 17:
        return "Production Failure"
    elif dice > 17 and dice <= 19:
        camp_size = ccamp.enemy_result()
        print(camp_size)
        return "Cult Activity"
    elif dice > 19 and dice <= 22:
        return "Diplomatic Envoy"
    elif dice > 22 and dice <= 25:
        return "Placeholder"
    elif dice > 25 and dice <= 27:
        return "Placeholder"
    elif dice > 27 and dice <= 28:
        return "Economic Surge"
    elif dice > 28 and dice <= 31:
        return "Expansion Demand"
    elif dice > 31 and dice <= 34:
        return "Festive Invitation"
    elif dice > 34 and dice <= 37:
        return "Feud"
    elif dice > 37 and dice <= 39:
        return "Food Shortage"
    elif dice > 39 and dice <= 42:
        return "Food Surplus"
    elif dice > 42 and dice <= 44:
        return "Good Weather"
    elif dice > 44 and dice <= 46:
        group_size = iparty.enemy_result()
        factions = ["The Guild", "Uscal", "Creibia", "Venizi"]
        faction = random.choice(factions)
        print(group_size)
        return (f"Inquisitors from {faction} are visiting")
    elif dice > 46 and dice <= 49:
        number = random.choice(range(20, 80))
        return (f"{number} poor immigrants have arrived at your castle")
    elif dice > 49 and dice <= 51:
        number = random.choice(range(10, 40))
        return (f"{number} immigrants have arrived at your castle")
    elif dice > 51 and dice <= 54:
        return "Local Disaster"
    elif dice > 54 and dice <= 57:
        monster = forest_hunt()
        print(monster)
        return "Monster Activity"
    elif dice == 58:
        return "Natural Disaster"
    elif dice > 58 and dice <= 61:
        return "Placeholder"
    elif dice > 61 and dice <= 64:
        return "New Subjects"
    elif dice > 64 and dice <= 67:
        pdemand = [200, 200, 500, 500, 500, 1000, 1000, 1250, 1500, 2500]
        demand = random.choice(pdemand)
        return (f"Guild Demands War funds: {demand} gold coins")
    elif dice > 67 and dice <= 70:
        return "Outstanding Success in Production"
    elif dice > 70 and dice <= 72:
        return "Pilgrimage"
    elif dice > 72 and dice <= 74:
        percentage = [1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 10]
        down = random.choice(percentage)
        return (f"Plague: {down}% of the population has come down with plague")
    elif dice > 74 and dice <= 78:
        return "Political Calm"
    elif dice > 78 and dice <= 81:
        return "Public Scandal"
    elif dice == 82:
        return "Remarkable Treasure"
    elif dice == 83:
        return "Cultist Sacrifices"
    elif dice > 83 and dice <= 85:
        return "Sensational Crime"
    elif dice > 85 and dice <= 90:
        camp_size = scamp.enemy_result()
        print(camp_size)
        return "Squatters have set up camp somewhere in the region"
    elif dice > 90 and dice <= 92:
        camp_size = ucamp.enemy_result()
        print(camp_size)
        return "Undead Uprising"
    elif dice > 92 and dice <= 95:
        return "Unexpected Find"
    elif dice > 95 and dice <= 97:
        return "Vandals"
    elif dice > 97 and dice <= 99:
        return "Visiting Celebrity"
    elif dice == 100:
        return "Wealthy Immigrant"