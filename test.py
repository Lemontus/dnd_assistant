import class_lib
from class_lib import *

herbs = {
    hgrass.name: hgrass.id,
    lleaf.name: lleaf.id
}

potions = {
    hwater.key: hwater
}

ingr_list = []

ingr1 = input()
if ingr1 in herbs:
    ingr1_id = str(herbs[ingr1])
    ingr_list.append(ingr1_id)
else:
    print("You suck")

ingr2 = input()
if ingr2 in herbs:
    ingr2_id = str(herbs[ingr2])
    ingr_list.append(ingr2_id)
else:
    print("You suck")

ingr3 = input()
if ingr3 in herbs:
    ingr3_id = str(herbs[ingr3])
    ingr_list.append(ingr3_id)
else:
    print("You suck")

ingr4 = input()
if ingr4 in herbs:
    ingr4_id = str(herbs[ingr4])
    ingr_list.append(ingr4_id)   
else:
    print("You suck")

ingr5 = input()
if ingr5 in herbs:
    ingr5_id = str(herbs[ingr5])
    ingr_list.append(ingr5_id)
else:
    print("You suck")

ingr_list.sort()
brew_key = "".join(ingr_list)

# for x in ingr_list:
#     brew_key = 


# brew_key = f"{ingr1_id}{ingr2_id}{ingr3_id}{ingr4_id}{ingr5_id}"

if brew_key in potions:
    print((potions[brew_key]).brew_potion())

# print(brew_key)
# print(list(herbs))
