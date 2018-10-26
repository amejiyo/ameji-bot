import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

client = discord.Client()
api = str(os.environ.get('RIOT_KEY'))

BOT_PREFIX = ("/")
client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    print('I am ready!')

@client.command(pass_context=True)
async def ping(ctx):
        await client.say("pong")


bot.run(os.environ['BOT_TOKEN'])
