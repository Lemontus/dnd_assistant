
import dictionaries
from dictionaries import *

# Potion Brewing function, used in brew command
def brew_func(ingr1, ingr2, ingr3, ingr4, ingr5, bonus):
    ingr_id_list = []

    if str.lower(ingr1) in herb_list:
        ingr1_id = str(herb_list[str.lower(ingr1)].id)
        ingr_id_list.append(ingr1_id)
        print(ingr_id_list)
    else:
        return
    
    if str.lower(ingr2) in herb_list:
        ingr2_id = str(herb_list[str.lower(ingr2)].id)
        ingr_id_list.append(ingr2_id)
        print(ingr_id_list)
    else:
        return
    
    if str.lower(ingr3) in herb_list:
        ingr3_id = str(herb_list[str.lower(ingr3)].id)
        ingr_id_list.append(ingr3_id)
        print(ingr_id_list)
    else:
        return
    
    if str.lower(ingr4) in herb_list:
        ingr4_id = str(herb_list[str.lower(ingr4)].id)
        ingr_id_list.append(ingr4_id)
        print(ingr_id_list)
    else:
        return
    
    if str.lower(ingr5) in herb_list:
        ingr5_id = str(herb_list[str.lower(ingr5)].id)
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
def item_look(name):
    if str.lower(name) in herb_list:
        herb_name = herb_list[str.lower(name)].description
        return herb_name

# Material Processing function used in the process command
def mat_processing(method, ingredient):
    if str.lower(method) == "grind":
    elif str.lower(method) == "dry":
    elif str.lower(method) == "smelt":
