
import dictionaries
from dictionaries import *

def brew_func(ingr1, ingr2, ingr3, ingr4, ingr5, bonus):
    ingr_id_list = []

    if str.lower(ingr1) in herb_list:
        ingr1_id = str(herb_list[str.lower(ingr1)])
        ingr_id_list.append(ingr1_id)
        print(ingr_id_list)
    else:
        return
    
    if str.lower(ingr2) in herb_list:
        ingr2_id = str(herb_list[str.lower(ingr2)])
        ingr_id_list.append(ingr2_id)
        print(ingr_id_list)
    else:
        return
    
    if str.lower(ingr3) in herb_list:
        ingr3_id = str(herb_list[str.lower(ingr3)])
        ingr_id_list.append(ingr3_id)
        print(ingr_id_list)
    else:
        return
    
    if str.lower(ingr4) in herb_list:
        ingr4_id = str(herb_list[str.lower(ingr4)])
        ingr_id_list.append(ingr4_id)
        print(ingr_id_list)
    else:
        return
    
    if str.lower(ingr5) in herb_list:
        ingr5_id = str(herb_list[str.lower(ingr5)])
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
