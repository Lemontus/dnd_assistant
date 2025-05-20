
import dictionaries
import class_lib
from dictionaries import *
from class_lib import *

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