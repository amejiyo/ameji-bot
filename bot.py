import discord
from discord.ext import commands
from discord.ext.commands import Bot

client = discord.Client()

BOT_PREFIX = ("/")
client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    print('I am ready!')

@client.command(pass_context=True)
async def ping(ctx):
        await client.say("pong")


client.run(BOT_TOKEN)
bot.run(BOT_TOKEN)
