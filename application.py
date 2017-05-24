import discord
from urllib.request import urlopen
from discord import channel
from plugins import utc
from plugins import callsign
from plugins import aprs

client = discord.Client()
help_msg = "Hello there! Below are my current functions.\r\n \r\n !call\r\n Usage: !call callsign_here\r\n Function: Return operator license details\r\n \r\n !utc\r\n Useage: !utc\r\n Function: Return UTC time\r\n \r\n !conditions\r\n Useage: !conditions\r\n Function: Return current ham radio conditions\r\n \r\n !aprs\r\n Usage: !aprs callsign callsign_rx_party passcode message\r\n Function: Send an aprs message, requires license. Use only in a private message!\r\n \r\n !iss \r\n Useage: !iss \r\n Function: Grab the current position of the international space station."

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name=' |!help'))


@client.event
async def on_message(message):
    if message.content.startswith('!help'):
        await client.send_message(message.channel, help_msg)  # line used to echo input not starting with [
    if message.content.startswith('!conditions'):
        #http://www.hamqsl.com/solarvhf.php" VHF
        img = urlopen("http://www.hamqsl.com/solar100sc.php").read()
        hand0 = open("conditions.jpg", "wb")
        hand0.write(img)
        hand0.close()
        await client.send_file(message.channel, 'conditions.jpg')
    if message.content.startswith('!iss'):
        #http://www.hamqsl.com/solarvhf.php" VHF
        issimg = urlopen("http://www2.heavens-above.com/orbitdisplay.aspx?icon=iss&width=300&height=300&satid=25544").read()
        hand0 = open("iss.gif", "wb")
        hand0.write(issimg)
        hand0.close()
        await client.send_message(message.channel, 'Here is the current position of the ISS')
        await client.send_file(message.channel, 'iss.gif')
    if message.content.startswith('!aprs'):
        await client.send_message(message.channel, 'Example: !aprs callsign sendcallsign passcode your message here')
        #!apre:kr0siv:wb5od:passcode:this is the message
        msg = message.content
        split = msg.split(None, 4)
        aprs_call = split[1]
        aprs_tocall = split[2]
        aprs_passcode = split[3]
        aprs_message = split[4]
        print(aprs_call, aprs_tocall, aprs_passcode, aprs_message)
        aprs_tosend = aprs.sendmsg(aprs_call, aprs_tocall, aprs_passcode, aprs_message)
        await client.send_message(message.channel, aprs_tosend)


    if message.content.startswith('!utc'):
        await client.send_message(message.channel, utc.get_time())
    if message.content.startswith('!call'):
        msg = message.content
        split = msg.split(' ')
        try:
            await client.send_message(message.channel, callsign.callsign_start(split[1]))
        except:
            await client.send_message(message.channel, "I'm sorry, was that a valid callsign?\r\nPlease check the call manually: http://radioreference.com/apps/ham/callsign/" + split[1])
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
