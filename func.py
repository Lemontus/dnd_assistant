
import dictionaries
import class_lib
import discord
from dictionaries import *
from class_lib import *
from discord import app_commands
from discord.ext import commands 
from typing import List

# Potion Brewing function, used in brew command
def brew_func(ingr1, ingr2, ingr3, ingr4, ingr5, bonus):
    ingr_id_list = []

    if str.lower(ingr1) in item_list:
        ingr1_id = str(item_list[str.lower(ingr1)].id)
        ingr_id_list.append(ingr1_id)
        print(ingr_id_list)
    else:
        return
    
    if str.lower(ingr2) in item_list:
        ingr2_id = str(item_list[str.lower(ingr2)].id)
        ingr_id_list.append(ingr2_id)
        print(ingr_id_list)
    else:
        return
    
    if str.lower(ingr3) in item_list:
        ingr3_id = str(item_list[str.lower(ingr3)].id)
        ingr_id_list.append(ingr3_id)
        print(ingr_id_list)
    else:
        return
    
    if str.lower(ingr4) in item_list:
        ingr4_id = str(item_list[str.lower(ingr4)].id)
        ingr_id_list.append(ingr4_id)
        print(ingr_id_list)
    else:
        return
    
    if str.lower(ingr5) in item_list:
        ingr5_id = str(item_list[str.lower(ingr5)].id)
        ingr_id_list.append(ingr5_id)
        print(ingr_id_list)
    else:
        return
    
    ingr_id_list.sort()
    potion_key = "".join(ingr_id_list)
    print(potion_key)

    if potion_key in potion_list:
        result = (potion_list[potion_key]).brew_potion(bonus)
        return result
    else:
        return "You have brewed an unknown potion"

# Item look up function, used in item look up command
def item_search(name):
    if str.lower(name) in item_list:
        herb_name = item_list[str.lower(name)].description
        return herb_name
    else:
        return "That's not a valid item name"

# Material Processing function used in the process command
def mat_processing(method, ingredient, bonus):
    if str.lower(method) == "grind":
        if str.lower(ingredient) in grind_list:
            result = grind_list[str.lower(ingredient)].process_material(bonus)
            return result
        else:
            return f"Can't grind {ingredient}"
    elif str.lower(method) == "dry":
        if str.lower(ingredient) in dry_list:
            result = dry_list[str.lower(ingredient)].process_material(bonus)
            return result
        else:
            return f"Can't dry {ingredient}"
    elif str.lower(method) == "smelt":
        if str.lower(ingredient) in smelt_list:
            result = smelt_list[str.lower(ingredient)].process_material(bonus)
            return result
        else:
            return f"Can't smelt {ingredient}"
    else:
        return f"{method} is not a valid method"
    

# Weather rolling function used in the Weather command
def forecast(location):
    if str.lower(location) == "lohsan":
        lwind = [nowind, nowind, nowind, nowind, nowind, lightwind, lightwind, lightwind, strongwind, strongwind]
        wind = random.choice(lwind)
        lpreci = [clearsky, clearsky, clearsky, clearsky, clearsky, clearsky, snow, snow, snow, snow]
        precipitation = random.choice(lpreci)
        if wind == strongwind and precipitation == snow:
            return f"There is a {blizzard.name} today, {blizzard.description}"
        else:
            return f"""Currently it's {precipitation.name}, {precipitation.description}
There is {wind.name}, {wind.description}"""
    else:
        return "It's not a valid location"
    
# Tax Collection function3
def tax_gather(poor, average, rich):
    tax = 0
    for x in range(poor):
        poor_money = random.choice(range(1, 7))
        print(poor_money)
        tax += poor_money
    for x in range(average):
        average_money = random.choice(range(3, 13))
        print(average_money)
        tax += average_money
    for x in range(rich):
        rich_money = random.choice(range(8, 26))
        print(rich_money)
        tax += rich_money
    return tax

# Rules embed function
def rules_embed(rule):
    if rule == "Basics":
        embed = discord.Embed(title="The Basics", url="https://homebrewery.naturalcrit.com/share/mluFPbOD3UXD", description="""The basics of roleplaying are as follows:

- To speak in-character please use “Quotation marks like this”
- To speak out-of-character please use (Parentheses like this)
- To roleplay in-character actions please use * Asterisks like this, but without space *
                              
All Roleplay happens in RP WORLD LOCATIONS category.""")
        
    elif rule == "Shields":
        embed = discord.Embed(title="Shields", url="https://homebrewery.naturalcrit.com/share/mluFPbOD3UXD", description="All Shields have designated bonus actions one can do with them, and each shield has different damate rating depending on their size and material its made of.")
        embed.add_field(name="Bonus Actions:", value="""- Buckler = 1AC passive. Bonus Action = Parry one attack until the start of your next turn (Disadvantage).

- Kite Shield = 1AC passive. Bonus Action = Actively defend to gain +2 AC until the start of your next turn.

- Tower Shield = 3 AC passive. Bonus Action = Full cover until the start of your next turn.

- Wall Shield = 4 AC passive. Whatever the heck it does because it’s already broken""")
        embed.add_field(name="Damage Rating:", value="""- Buckler = 1d4

- Kite Shield = 1d6

- Tower Shield = 1d8 Disadvantage

- Wall Shield = 20 STR - 1d20 You can do a crit/double crit on someone that is prone with the spikes at the bottom""")
        
    elif rule == "Cover":
        embed = discord.Embed(title="Cover", url="https://homebrewery.naturalcrit.com/share/mluFPbOD3UXD", description="""Walls, trees, creatures, and other obstacles can provide cover during combat, making a target more difficult to harm. A target can benefit from cover only when an attack or other effect originates on the opposite side of the cover.

There are three degrees of cover. If a target is behind multiple sources of cover, only the most protective degree of cover applies; the degrees aren’t added together. For example, if a target is behind a creature that gives half cover and a tree trunk that gives three-quarters cover, the target has three-quarters cover.

A target with half cover has a +2 bonus to AC and Dexterity saving throws. A target has half cover if an obstacle blocks at least half of its body. The obstacle might be a low wall, a large piece of furniture, a narrow tree trunk, or a creature, whether that creature is an enemy or a friend.

A target with three-quarters cover has a +5 bonus to AC and Dexterity saving throws. A target has three-quarters cover if about three-quarters of it is covered by an obstacle. The obstacle might be a portcullis, an arrow slit, or a thick tree trunk.

A target with total cover can’t be targeted directly by an attack or a spell, although some spells can reach such a target by including it in an area of effect.""", color=0xFF5733)
        
    elif rule == "Spells":
        embed = discord.Embed(title="Reworked Spells: Bonus Action", url="https://homebrewery.naturalcrit.com/share/mluFPbOD3UXD", description="A spell cast with a bonus action is especially swift. You must use a bonus action on your turn to cast the spell, provided that you haven’t already taken a bonus action this turn. Unlike the basic rules, you can cast another spell during the same turn, regardless of whether it is a levelled spell or a cantrip, with a casting time of 1 action.")

    elif rule == "Suffocating":
        embed = discord.Embed(title="Suffocating", url="https://homebrewery.naturalcrit.com/share/mluFPbOD3UXD", description="""A creature can hold its breath for a number of minutes equal to 1 + its Constitution modifier (minimum of 30 seconds)

Each hit the creature receives substracts that number by 1 minute.

When a creature runs out of breath or is choking, it can survive for a number of rounds equal to its Constitution modifier (minimum of 1 round). At the start of its next turn, it drops to 0 hit points and is dying, and it can’t regain hit points or be stabilized until it can breathe again.""")

    elif rule == "Gnomes":
        embed = discord.Embed(title="Gnomes", url="https://homebrewery.naturalcrit.com/share/mluFPbOD3UXD", description="All gnomes are considered objects when a Catapult spell is cast on them.")

    elif rule == "High Ground":
        embed = discord.Embed(title="High Ground", url="https://homebrewery.naturalcrit.com/share/mluFPbOD3UXD", description="When you attack from above, you gain a **+2 bonus** to the Attack Roll. When you attack from below, you have a **-2 penalty**. The Height Difference between you and your target must be at least **2.5m / 10ft**")

    elif rule == "Magical Effects":
        embed = discord.Embed(title="Combining Magical Effects", url="https://homebrewery.naturalcrit.com/share/mluFPbOD3UXD", description="""The effects of different spells add together while the durations of those spells overlap. The effects of the same spell cast multiple times don’t combine.

For example, if two clerics cast bless on the same target, that character gains the spell’s benefit only once; he or she doesn’t get to roll two bonus dice.""")
        
    elif rule == "Jump":
        embed = discord.Embed(title="Jump", url="https://homebrewery.naturalcrit.com/share/mluFPbOD3UXD", description="Jump distance with 8 STR is 15ft. Additionally, jump distance does not start increasing until you reach 12 STR, where it increases by 2.5ft, and then goes up by 2.5ft every 2 points of STR past that. Odd numbers of STR have no bearing on jump distance whatsoever. Costs a bonus action to use.")

    elif rule == "Wounded":
        embed = discord.Embed(title="Wounded", url="https://homebrewery.naturalcrit.com/share/mluFPbOD3UXD", description="""You have been seriously injured. If your hit points raise above 0 and you do not already have the wounded condition, you become wounded 1. If you already have the wounded condition when you lose the dying condition, your wounded condition value increases by 1. Wounded condition gives **-2 penalty** to all rolls for every stack of Wounded Condition
The wounded condition ends if someone successfully uses a DC 10 medicine check, or if you are restored to full Hit Points and rest for 10 minutes.""")

    elif rule == "Cold":
        embed = discord.Embed(title="Cold", url="https://homebrewery.naturalcrit.com/share/mluFPbOD3UXD", description="""Regions situated in areas with permanent winter, and most other regions in the season of Winter are extremely cold, due to that one is required to wear warm clothes, or keep warming potions in stock as protection from the extreme temperatures.

Without protection, following debuffs will be applied:

- Disadvantage on all skill checks.
- Disadvantage on attack rolls.
- Disadvantage on saving throws.
- Possibility of passing out (Con save every ingame hour)
                              
Additionally, without proper footwear in deep snow the following applies:

- Movement speed is halved.""")

    elif rule == "Opportunity Attacks":
        embed = discord.Embed(title="Opportunity Attacks", url="https://homebrewery.naturalcrit.com/share/mluFPbOD3UXD", description="In addition to standard Attack of Opportunity rules, you can attack an opponent attempting to walk past or around you within your reach.")

    elif rule == "Study":
        embed = discord.Embed(title="Study (Action)", url="https://homebrewery.naturalcrit.com/share/mluFPbOD3UXD", description="""When you take the Study action, you make an Intelligence check to study your memory, a book, a creature, a clue, an object, or another source of knowledge and call to mind an important piece of information about it.
The Areas of Knowledge table suggests which skills are applicable when you take this action, depending on the area of knowledge the Intelligence check is about.""")
        embed.add_field(name="**AREAS OF KKNOWLEDGE**",value="", inline=False)
        embed.add_field(name="Skill", value="""Arcana 



History         
                        
Investigation 
Nature 
                        
Religion                
                        """, inline=True)
        embed.add_field(name="Areas", value="""Spells, magic items, eldritch symbols, magical traditions, planes of existence, and certain creatures (Aberrations, Constructs, Elementals,Fey, and Monstrosities)

Historic events and people, ancient civilizations, wars, and certain creatures (Giants and Humanoids)
Traps, ciphers, riddles, and gadgetry
Terrain, flora, weather, and certain creatures (Beasts, Dragons, Oozes, and Plants)
Deities, religious hierarchies and rites,holy symbols, cults, and certain creatures (Celestials, Fiends, and Undead)


                        """, inline=True)
        
    elif rule == "Grapple":
        embed = discord.Embed(title="Grappled(Condition)", url="https://homebrewery.naturalcrit.com/share/mluFPbOD3UXD", description="While Grappled you experience the following effects:")
        embed.add_field(name="Speed 0", value="Your Speed is 0 and can't change", inline=False)
        embed.add_field(name="Attacks Affected", value="You have Disadvantage on attack rolls against any target other than the grappler", inline=False)
        embed.add_field(name="Movable", value="The grappler can drag or carry you when it Moves, but every foot of movement costs it 1 extra foot unless you are Tiny or two or more sizes smaller than the grappler.", inline=False)
        embed.add_field(name="Escape", value="While Grappled, you can use your action to make a Strength (Athletics) or Dexterity (Acrobatics) check against the grapple’s escape DC, ending the condition on yourself on a success. The condition also ends if the grappler has the Incapacitated condition or if the distance between you and the grappler exceeds the grapple’s range.", inline=False)

    elif rule == "Hide":
        embed = discord.Embed(title="Hide (Action)", url="https://homebrewery.naturalcrit.com/share/mluFPbOD3UXD", description="""With the Hide action, you try to conceal yourself. To do so stealthily, you must succeed on a DC 15 Dexterity (Stealth) check while you’re Heavily Obscured or behind Three-Quarters Cover or Total Cover, and you must be out of any visible enemy’s line of sight; if you can see a creature, you can discern whether it can see you.

On a successful check, you have the Invisible condition. Make note of your check’s total, which becomes the DC for a creature to find you with a Wisdom (Perception) check.

The condition ends on you immediately after any of the following occurrences: you make a sound louder than a whisper, an enemy finds you, you make an attack roll, or you cast a spell with a verbal component.""")
        
    elif rule == "Invisible":
        embed = discord.Embed(title="Invisible (Condition)", url="https://homebrewery.naturalcrit.com/share/mluFPbOD3UXD", description="While Invisible you experience the following effects:")
        embed.add_field(name="Concealed", value="You aren't affected by any effect that requires its target to be seen", inline=False)
        embed.add_field(name="Surprise", value="If you're Invisible when you roll Initiative, you have Advantage on the roll", inline=False)
        embed.add_field(name="Attacks Affected", value="Attack rolls against you have Disadvantage, and your attack rolls have Advantage. If a creature can somehow see you, as with magic or Blindsight, you don’t gain this benefit against that creature.", inline=False)

    elif rule == "Knocking Out":
        embed == discord.Embed(title="Knocking out a Creature", url="https://homebrewery.naturalcrit.com/share/mluFPbOD3UXD", description="""Sometimes an attacker wants to knock out a foe rather than deal a killing blow. When an attacker would reduce a creature to 0 Hit Points with a melee attack, the attacker can instead reduce the creature to 1 Hit Point. The creature then has the Unconscious condition and starts a Short Rest.

The creature remains Unconscious until it regains any Hit Points or until someone uses an action to administer first aid to it, which requires a successful DC 10 Wisdom (Medicine) check.""")

    elif rule == "Search":
        embed = discord.Embed(title="Search (Action)", url="https://homebrewery.naturalcrit.com/share/mluFPbOD3UXD", description="When you take the Search action, you make a Wisdom check to discern something that isn’t obvious. The Search table suggests which skills are applicable when you take this action, depending on what you’re trying to detect.")
        embed.add_field(name="SEARCH", value="", inline=False)
        embed.add_field(name="Skill", value="""Insight
Medicine
Perception
Survival""", inline=True)
        embed.add_field(name="Things to Detect", value="""Creature's state of mind
Creature's ailment
Concealed creature or object
Tracks or food""", inline=True)

    return embed

# Info Function
def info1_embed(category):
    embed = discord.Embed(title="Selling Treasure", url="https://homebrewery.naturalcrit.com/share/mluFPbOD3UXD", description="Opportunities abound to find treasure, equipment, weapons, armor, and more in the dungeons you explore. Normally, you can sell your treasures and trinkets when you return to a town or other settlement, provided that you can find buyers and merchants interested in your loot.")
    if category == "Military":
        embed.add_field(name="Arms, Armor, and Other Equipment", value="As a general rule, undamaged weapons, armor, and other equipment fetch half their cost when sold in a market. Weapons and armor used by monsters are rarely in good enough condition to sell for much. Locations such as military outposts, and war camps will usually buy such equipment for a higher price than merchants at a market.")
    elif category == "Magic Items":
        embed.add_field(name="Magic Items", value="Selling magic items is problematic. Finding someone to buy a potion or a scroll isn’t too hard, but other items are out of the realm of most but the wealthiest nobles. Likewise, aside from a few common magic items, you won’t normally come across magic items or spells to purchase.")
    elif category == "Luxuries":
        embed.add_field(name="Gems, Jewelry and Art Objects", value="These items retain their full value in the marketplace, and you can either trade them in for coin or use them as currency for other transactions. For exceptionally valuable treasures, the DM might require you to find a buyer in a large town or larger community first.")
    elif category == "Trade Goods":
        embed.add_field(name="Trade Goods and Other", value="On the borderlands, many people conduct transactions through barter. Like gems and art objects, trade goods—bars of iron, bags of salt, livestock, and so on—retain their full value in the market and can be used as currency.")
    else:
        return "That is not a valid category"

    return embed    