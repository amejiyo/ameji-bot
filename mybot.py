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


client = Bot(command_prefix=BOT_PREFIX)

newUserDMMessage = "Welcome to LOUDHOUSE"


#voice command

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('/hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('/pretty'):
        await client.send_message(message.channel, "Ameji is beautiful girl")
    if message.content.startswith('/yemo'):
        await client.send_message(message.channel, 'The old man?')
        msg = await client.wait_for_message(author=message.author, content='oops')
        await client.send_message(message.channel, ';P')
    if message.content.startswith('/rule'):
        msg = "Faction rules: \n 1. Prob and audit only target faction or serve faction. \n2. Weekly credit must be more than 1000 per week. \n3. Respond to higher-ups at 7:30-8:30. \n4. Don't  be offline continuously 3 days (or more than). \nIf you are busy or want any excuse contact elites, home secretary, deputy, diplomat \n\nThe punishment \nkick"
        await client.send_message(message.channel, msg)
    elif message.content.startswith('/bug'):
        await client.send_message(message.channel, 'Please contact ameji')

    if message.content.startswith('/cool'):
        await client.send_message(message.channel, 'Who is cool? Type @name')
        def check(msg):
            return msg.content.startswith('{0.author.mention}'.format(message))
        message = await client.wait_for_message(author=message.author, check=check)
        await client.send_message(message.channel, '{0.author.mention} is cool indeed'.format(message))

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))

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

bot.run(os.environ['BOT_TOKEN'])
