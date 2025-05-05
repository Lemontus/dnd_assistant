# dnd_assistant
DnD Assistant is a discord bot.

## Gather Command
- Gather command is used for herb gathering.
- It takes the "location" argument and a "bonus" argument.
- It uses the "location" argument to determine where the user wants to look for herbs.
- Once a location is determined, it then picks a random number from 1 to 100 (using random module) to determine what the user has found based on the "roll table" of that location.
- Once that has been determined, the command then determines how many items have been gathered, it picks a random number from 1 to 20, adds the "bonus" argument to the result and checks it against the difficulty of the item.
- If the result meets the difficulty, it adds 1 item to the total number of gathered items every even number above the difficulty up to the maximum available.
- It then returns a string telling the user what he has found, and how many items he has gathered.

## Mine Command
- Mine Command is the same as Gather Command but is used for mining instead of herb gathering.

## Brew Command
- Brew Command is used for potion brewing.
- It takes 5 ingredient arguments and an additional "bonus" argument.
- It checks each ingredient argument against the herb_list dictionary that houses all available herbs to determine if it exists.
- If the ingredient matches any available herbs, it then adds the id of the herb taken from the dictionary into a list.
Once all ingredients have been checked, it sorts the list from lowest to highest number, then turns it into a string and puts it into the potion_key variable.
- The potion_key variable is then checked against the potion_list.
- If the potion_key matches any potion key present in potion_list, it runs the brew_potion function of that potion.
- The function then picks a random number from 1 to 20 and adds the "bonus" argument to the result.
- The result is then compared to the difficulty to see if it's equal or greater.
- If it is then the brewing is a success and it returns a string indicating so, the string is then sent to the user as a discord message that only they can see (using ephemeral function from discord.py)