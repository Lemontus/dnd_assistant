import os
import random
import sqlite3
import time
import discord
import roll_tables
import class_lib
from class_lib import *
from roll_tables import *
from func import *
from dotenv import load_dotenv

from discord import app_commands
from discord.ext import commands 
from typing import List


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
client = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord')

# Dice rolling command
@bot.hybrid_command(name='dice', help='rolls dice')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

# Herb Gathering Command
@bot.hybrid_command(name="gather", help="The gathering command accepts, Locations: Plains, Forest")
async def herbs(ctx, location: str, bonus: int):
    dice = random.choice(range(1, 101))
    if location == "Plains" or location == "plains":
        patch = plains_herb(dice, bonus)
    elif location == "Forest" or location == "forest":
        patch = forest_herb(dice, bonus)
    else:
        await ctx.send("That's not a location")
        return

    await ctx.send(f"You rolled {dice}")
    await ctx.send(patch)

@herbs.autocomplete("location")
async def herbs_autocomplete(interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
    options = ["Plains", "Forest"]
    return [app_commands.Choice(name=option, value=option) for option in options if option.lower().startswith(current.lower())][:25]

# Mineral Gathering Command
@bot.hybrid_command(name="mine", help="The Mining command accepts, Locations: Plains, Forest")
async def metals(ctx, location, bonus=0):
    dice = random.choice(range(1, 101))
    if location == "Plains" or location == "plains":
        vein = plains_metal(dice, bonus)
    elif location == "Forest" or location == "forest":
        vein = forest_metal(dice, bonus)
    else:
        await ctx.send("That's not a location")
        return
    await ctx.send(f"You rolled {dice}")
    await ctx.send(vein)

@metals.autocomplete("location")
async def metals_autocomplete(interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
    options = ["Plains", "Forest"]
    return [app_commands.Choice(name=option, value=option) for option in options if option.lower().startswith(current.lower())][:25]

# Potion Brewing Command
@bot.hybrid_command(name="brew", help="The Brew command accepts")
async def potions(ctx, ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, bonus=0):
    print(f"{ingredient1}, {ingredient2}, {ingredient3}, {ingredient4}, {ingredient5}")
    result = brew_func(ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, bonus)

    await ctx.send(f"{result}", ephemeral=True)
    await ctx.send(f"{ctx.author.mention} is currently brewing potions")

# Blacksmithing Command
@bot.hybrid_command(name="smith", help="The Smith command is used for blacksmithing")
async def smithing(ctx, target, bonus):
    print(target, bonus)

# Blacksmithing Recipe Check Command
@bot.hybrid_command(name="recipe", help="The Recipe command is used for checking what can be crafted at what lvl, Methods: blacksmithing")
async def recipe_check(ctx, method, level):
    print(method, level)
    if str.lower(method) == "blacksmithing":
        pass


# Material Processing Command
@bot.hybrid_command(name="process", help="The Process command is used for processing materials, Methods: dry, grind, smelt")
async def processing(ctx, method, ingredient, how_many:int, bonus:int):
    print(method, ingredient,how_many, bonus)
    n = how_many
    for i in range(0, n):
        result = mat_processing(method, ingredient, bonus)

        await ctx.send(f"{result}", ephemeral=True)
        time.sleep(1)
    await ctx.send(f"{ctx.author.mention} is currently processing materials")

# Item Lookup Command
@bot.hybrid_command(name="search")
async def herbs(ctx, name):
    print(name)
    result = item_search(name)

    await ctx.send(f"{result}")

# Random Weather Command
@bot.hybrid_command(name="weather")
async def weather(ctx, location):
    print(location)
    fcast = forecast(location)

    await ctx.send(f"{fcast}")

@weather.autocomplete("location")
async def weather_autocomplete(interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
    options = ["lohsan"]
    return [app_commands.Choice(name=option, value=option) for option in options if option.lower().startswith(current.lower())][:25]

# General Kingdom Management Command
@bot.hybrid_command(name="kingdom")
async def kingdom(ctx, command):
    print(command)
    if command == "event":
        dice = random.choice(range(1, 101))
        event = k_events(dice)

        await ctx.send(f"{event}")
    elif command == "tax":
        poor = 80
        average = 15
        rich = 1
        taxes = tax_gather(poor, average, rich)

        await ctx.send(f"You have gathered {taxes} gold coins as tax")

@kingdom.autocomplete("command")
async def kingdom_autocomplete(interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
    options = ["event", "tax"]
    return [app_commands.Choice(name=option, value=option) for option in options if option.lower().startswith(current.lower())][:25]

# Rules Command
@bot.hybrid_command(name="rules")
async def rules(ctx, rule):
    embed = rules_embed(rule)
    embed.set_footer(text="Don't be a dingus and read carefully.")

    await ctx.send(embed = embed)

@rules.autocomplete("rule")
async def rules_autocomplete(interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
    options = ["Cover", "Shields", "Basics", "Spells", "Suffocating", "Gnomes", "High Ground", "Magical Effects", "Jump", "Wounded", "Cold", "Opportunity Attacks", "Study", "Grapple", "Hide", "Invisible", "Knocking Out", "Search"]
    return [app_commands.Choice(name=option, value=option) for option in options if option.lower().startswith(current.lower())][:25]

# Info Command
@bot.hybrid_group(name="info")
async def info(ctx: commands.Context) -> None:
    await ctx.send("Information Command")

@bot.hybrid_command(name="selling_treasure")
async def info_1(ctx, category):
    embed = info1_embed(category)

    await ctx.send(embed = embed)

#@info_1.autocomplete("category")
#async def info_1_autocomplete(interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
#    options = ["Military", "Magic Items", "Luxuries", "Trade Goods"]
#    return [app_commands.Choice(name=option, value=option) for option in options if option.lower().startswith(current.lower())][:25]

@bot.hybrid_command(name="database")
async def database(ctx):

    sqlite_connection = sqlite3.connect('The Guild')
    cursor = sqlite_connection.cursor()
    print('DB Init')

    #cursor.execute("INSERT INTO Material VALUES ('Life Leaf Pulp', 'It is green', 8, 23, 'Life Leaf'), ('Dried Life Leaf', 'It is green', 8, 24, 'Life Leaf')")
    #sqlite_connection.commit()

    res = cursor.execute("select Name from Material")
    result = res.fetchall()
    await ctx.send(result)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Ready!")

# @bot.command(name='create-channel')
# @commands.has_role('admin')
# async def create_channel(ctx, channel_name='new channel'):
#     guild = ctx.guild
#     existing_channel =discord.utils.get(guild.channels, name=channel_name)
#     if not existing_channel:
#         print(f'Creating a new channel: {channel_name}')
#         await guild.create_text_channel(channel_name)

# @bot.event
# async def on_command_error(ctx, errfrom discord import app_commands
# from discord.ext import commands 
# from typing import Listor):
#     if isinstance(error, commands.errors.CheckFailure):
#         await ctx.send('You do not have the correct role for this')


bot.run(TOKEN)

# TypeError, found fix here https://shorturl.at/ALSsg, better way to write it here https://www.reddit.com/r/discordbots/comments/11svqp6/bot_doesnt_recognize_or_respond_to_prefix/

client = discord.Client(intents=discord.Intents.all())

# @client.event
# async def on_ready():
#     guild = discord.utils.get(client.guilds, name=GUILD)
# # loops through client.guilds to find the guild(server) provided in .env
#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})'
    # )
# loops through the guild.members, prints out the members inside the guild - Need to fix, only shows itself
    # members = '\n - '.join([member.name for member in guild.members])
    # print(f'Guild Members:\n - {members}')

# @client.event
# async def on_ready():
#     print(f'{client.user.name} has connected to Discord!')

# Creates then sends a message to every user that joins the discord guild/server
# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server!'
#     )remember-to-put-discord-token-here

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
    
#     brooklyn_99_quotes = [
#         'I\'m the human form of the 💯 emoji.',
#         'Bingpot!',
#         (
#             'Cool. cool cool cool cool cool cool cool,'
#             'no doubt no doubt no doubt no doubt.'
#         ),
#     ]

#     if message.content == '99!':
#         response = random.choice(brooklyn_99_quotes)
#         await message.channel.send(response)
#     elif message.content == 'raise-exception':
#         raise discord.DiscordException
    
# @client.event
# async def on_error(event, *args, **kwargs):
#     with open('err.log', 'a') as f:
#         if event == 'on_message':
#             f.write(f'Unhandled message: {args[0]}\n')
#         else:
#             raise

client.run(TOKEN)