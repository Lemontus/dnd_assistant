import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# TypeError, found fix here https://shorturl.at/ALSsg, upon further inspection issue was old tutorial, fix found here: https://www.reddit.com/r/Discord_Bots/comments/k3l0b1/discordpy_cant_get_guild_members/
intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
# loops through client.guilds to find the guild(server) provided in .env
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
# loops through the guild.members, prints out the members inside the guild - Need to fix, only shows itself
    # members = '\n - '.join([member.name for member in guild.members])
    # print(f'Guild Members:\n - {members}')

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

# Creates then sends a message to every user that joins the discord guild/server
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

client.run(TOKEN)