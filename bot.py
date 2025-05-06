import os
import random

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
@bot.hybrid_command(name="gather", help="The gathering command accepts !gather + <location> + <bonus>")
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

# Mineral Gathering Command
@bot.hybrid_command(name="mine", help="The Mining command accepts !mine + <location> + <bonus>")
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

# Potion Brewing Command
@bot.hybrid_command(name="brew", help="The Brew command accepts !brew + ")
async def potions(ctx, ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, bonus=0):
    print(f"{ingredient1}, {ingredient2}, {ingredient3}, {ingredient4}, {ingredient5}")
    result = brew_func(ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, bonus)

    await ctx.send(f"{result}", ephemeral=True)
    await ctx.send(f"{ctx.author.mention} is currently brewing potions")

# Material Processing Command
@bot.hybrid_command(name="process", help="The Process command is used for processing materials")
async def processing(ctx, method, ingredient, bonus:int):
    print(method, ingredient, bonus)
    result = mat_processing(method, ingredient, bonus)

    await ctx.send(f"{result}", ephemeral=True)
    await ctx.send(f"{ctx.author.mention} is currently processing materials")

# Herb Lookup Command
@bot.hybrid_command(name="herb")
async def herbs(ctx, name):
    print(name)
    result = item_look(name)

    await ctx.send(f"{result}")

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
# async def on_command_error(ctx, error):
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