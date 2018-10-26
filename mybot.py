import random
import discord
import requests
import asyncio
from discord import Game
from discord.ext import commands
import logging
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient

BOT_PREFIX = ("/")

TOKEN = BOT_TOKEN

client = Bot(command_prefix=BOT_PREFIX)

newUserDMMessage = "Welcome to LOUDHOUSE"


#voice command

#8ball game
@client.command(name= '8ball',
                description="Answer a yes/no question.",
                brief="Answer from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell'''
        'It is quite possible'''
        '"Definitely'
    ]
    await client.say(random.choice(possible_responses) + "," + context.message.author.mention)

#game
@client.command(name= 'tellme',
                description="Answer a yes/no question.",
                brief="Answer from the beyond.",
                aliases=['answer', 'ans', 'ANSWER', 'TellMe', 'Tell_Me'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'You look as pretty as always',
        'Too hard to tell',
        'You are very beautiful',
        'So ugly',
        'I think you are very attractive',
        'Wow, you are gorgeous',
        'I think you are stunning!',
        'I think you are super cute',
        'You are beyond gorgeous',
        'Your beauty is incomparable',
        'You look like an angel',
        'At least your hair is nice!',
        'It looks like someone lit a FIRE on your face and put it out with a pitch fork and a golf shoe!',
        'I was feeling sorry for myself....until I saw you',
    ]
    await client.say(random.choice(possible_responses) + "," + context.message.author.mention)

@client.command(name= 'square')
async def square(number):
    square_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(square_value))

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Any error tell ameji"))
    print("Logged in as " + client.user.name)

@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    respond = requests.get(url)
    value = respond.json()['bpi']['USD']['rate']
    await client.say("Bitcoin price is: $" + value)
async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers: ")
        for server in client.servers:
            print(server.name)
        break
        await asyncio.sleep(6)

client.loop.create_task(list_servers())

client.run(TOKEN)
bot.run(TOKEN)
