from urllib.request import urlopen
from discord import channel

def conditions():
    img = urlopen("http://www.hamqsl.com/solar100sc.php").read()
    hand0 = open("conditions.jpg", "wb")
    hand0.write(img)
    hand0.close()
    await
    client.send_file(message.channel, 'conditions.jpg')
