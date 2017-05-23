import discord
import asyncio
from plugins import utc
from plugins import callsign

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!help'):
        await client.send_message(message.channel, "Just a basic bot to answer simple radio queries")  # line used to echo input not starting with [
    if message.content.startswith('!utc'):
        await client.send_message(message.channel, utc.get_time())
    if message.content.startswith('!call'):
        msg = message.content
        split = msg.split(' ')
        await client.send_message(message.channel, callsign.callsign_start(split[1]))
    else:
        pass


def start_discord():
    with open('C:\config.txt', 'r') as myfile:
        config_file = myfile.read().replace('\n', '')
    client.run(config_file)

start_discord()


#await client.send_message(message.channel, 'var1: ' + split[0])
#await client.send_message(message.channel, 'var2: ' + split[1])
#print('msg.split var' + split[0])
#print('msg.split var' + split[1])
