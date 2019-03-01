import asyncio
import os
import youtube_dl
import discord
from discord.ext import commands
songs = asyncio.Queue()
play_next_song = asyncio.Event()

client = commands.Bot(command_prefix = '.')
players ={}
queues = {}

@client.event
async def on_ready():
    print('Logged in as:\n{0}'.format(client.user))
async def audio_player_task():
    while True:
        play_next_song.clear()
        current = await songs.get()
        current.start()
        await play_next_song.wait()

def toggle_next():
    client.loop.call_soon_threadsafe(play_next_song.set)

@client.command(pass_context =True)
async def join(ctx):
    channel = ctx.message.author.voice_channel
    await client.join_voice_channel(channel)
    await client.say("the dummy has joined the voice channel.")
@client.command(pass_context =True)
async def leave (ctx):
   server = ctx.message.server
   voice_client = client.voice_client_in(server)
   await voice_client.disconnect()
   await client.say("the dummy has left the voice channel.")
@client.command(pass_context = True)
async def play(ctx, url):
   channel = ctx.message.author.voice_channel
   while not client.is_voice_connected(channel):
       await client.join_voice_channel(channel)
       await client.say("the dummy has joined the voice channel.")
       break
   server = ctx.message.server
   voice_client = client.voice_client_in(server)
   player = await voice_client.create_ytdl_player(url)
   players[server.id] = player
   player.start()
   await client.say("the dummy is playing "+ url +" right now.")

@client.command(pass_context = True)
async def loop(ctx):
    while True:
        id = ctx.message.server.id
        players[id].start()
        if ctx.message.content.startswith('/stop'):
            break


@client.command(pass_context = True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()
@client.command(pass_context = True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()
@client.command(pass_context = True)
async def skip(ctx):
    id = ctx.message.server.id
    await client.say("The song " + str(players) + " was skipped.")
    players[id].stop()

@client.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(client.user))

client.run(os.environ['BOT_TOKEN'])
