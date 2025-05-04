import dictionaries
from dictionaries import *

def brew_func(ingr1, ingr2, ingr3, ingr4, ingr5, bonus):
    ingr_id_list = []

    if ingr1 in herb_list:
        ingr1_id = str(herb_list[ingr1])
        ingr_id_list.append(ingr1_id)
    else:
        return
    
    if ingr2 in herb_list:
        ingr2_id = str(herb_list[ingr2])
        ingr_id_list.append(ingr2_id)
    else:
        return
    
    if ingr3 in herb_list:
        ingr3_id = str(herb_list[ingr3])
        ingr_id_list.append(ingr3_id)
    else:
        return
    
    if ingr4 in herb_list:
        ingr4_id = str(herb_list[ingr4])
        ingr_id_list.append(ingr4_id)
    else:
        return
    
    if ingr5 in herb_list:
        ingr5_id = str(herb_list[ingr5])
        ingr_id_list.append(ingr5_id)
    else:
        return
    
    ingr_id_list.sort()
    potion_key = "".join(ingr_id_list)

    if potion_key in potion_list:
        return(potion_list[potion_key]).brew_potion(bonus)
    else:
        return "You have brewed an unknown potion"
