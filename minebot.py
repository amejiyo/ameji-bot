import discord

client = discord.Client()
TOKEN = "NTAzODE4MjQzODA3NjQxNjIy.Dq8-ww.MiviRJBbYt30IF8gBhQ0uag75cE"
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
        await client.send_message(message.channel, 'Who is cool? Type /name')
        def check(msg):
            return msg.content.startswith('{0.author.mention}'.format(message))
        message = await client.wait_for_message(author=message.author, check=check)
        await client.send_message(message.channel, '{0.author.mention} is cool indeed'.format(message))

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)