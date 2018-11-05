import random
import discord
import requests
import asyncio
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot
import os
from discord import Game
me = 'Ameji'
me = 'ameji'

client = discord.Client()
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
        msg = await client.wait_for_message(author=message.author, content=['oops','Opps','meh', 'Mehh', 'Meh','Oops'])
        await client.send_message(message.channel, ';P')
    if message.content.startswith('/rule'):
        msg = "Faction rules: \n 1. Prob and audit only target faction or serve faction. \n2. Weekly credit must be more than 1000 per week. \n3. Respond to higher-ups at 7:30-8:30. \n4. Don't  be offline continuously 3 days (or more than).\n5. Don't snipe other players. We have a schedule. If you want a date plz book it in #dating-schedule .\n If you are busy or want any excuse contact elites, home secretary, deputy, diplomat \n\nThe punishment \nkick"
        await client.send_message(message.channel, msg)
    if message.content.startswith('/kick'):
        msg = "You stay offline continuously for 5 days which against our rules. However, if you would like to join us again, apply LH. I will always wait for your returning.\n\nSorry,\nAmeji."
        await client.send_message(message.channel, msg)
    elif message.content.startswith('/bug'):
        await client.send_message(message.channel, 'Please contact ameji')

    if message.content.startswith('/cool'):
        await client.send_message(message.channel, 'Who is cool? Type /name')
        def check(msg):
            return msg.content.startswith('{0.author.mention}'.format(message))
        message = await client.wait_for_message(author=message.author, check=check)
        await client.send_message(message.channel, '{0.author.mention} is cool indeed'.format(message))
    if message.content.startswith('/approve'):
        msg = "Thanks for applying to this faction. Before I approved you, I would like to introduce you LOUDHOUSE's rules. Please probe and audit only target faction or serve faction (a Chinese name), and do the guild's quest. \n\nPlease reply to this mail as confirmation.\n\nBest regard,\nAmeji."
        await client.send_message(message.channel, msg)
    #waifu
    if message.content.startswith('/waifu'):
        await client.send_message(message.channel, 'You? ')
        def check(msg):
            return msg.content.startswith('{0.author.mention}'.format(message))
        message = await client.wait_for_message(author=message.author)

        if message.author.id == os.environ['ameji']:
            await client.send_message(message.channel, '100% for my beloved lord.')
        if message.content == me:
            await client.send_message(message.channel, '100% for my lovely lord')
        else:
            possible_responses = [
            'Error 404: not found',
            'Between a trash and you, I will choose a trash.',
            'I cant rate. You are incomparable.',
            'No one is better than you.',
            'Who dare to marry you?',
            '50%',
            'Give meimei a big red packet first',
            'I am lazy now',
            'Why do I need to rate you?'
            ]
            ans = '{0.author.mention}'.format(message)
            await client.send_message(message.channel, random.choice(possible_responses) + ' ' + ans)

      
@client.event
async def on_member_join(member):
    server = member.server
    channel = member.server.get_channel(os.environ['CHANNEL_ID'])
    fmt = 'Welcome {0.mention} to {1.name}, please read the message at new-member-discord-guide and enjoy your stay.'
    await client.send_message(channel, fmt.format(member, server))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(os.environ['BOT_TOKEN'])
