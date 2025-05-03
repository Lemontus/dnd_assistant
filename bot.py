import os
import random

import time
import discord
import herb_spots
from herb_spots import *
from dotenv import load_dotenv

from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord')

@bot.hybrid_command(description="Bot's latency")
async def ping(ctx):
    await ctx.respond(f'pong! Latency is {bot.latency}')


@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. cool cool cool cool cool cool cool,'
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='roll_dice', help='rolls dice')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name="gather", help="Test command")
async def herbs(ctx, location, bonus=0):
    dice = random.choice(range(1, 101))
    if location == "Plains" or location == "plains":
        patch = plains(dice, bonus)
    else:
        await ctx.send("That's not a location")
        return

    await ctx.send(f"You rolled {dice}")
    # time.sleep(1)
    await ctx.send(patch)
    # time.sleep(1)

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

# client = discord.Client(intents=discord.Intents.all())

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

# client.run(TOKEN)