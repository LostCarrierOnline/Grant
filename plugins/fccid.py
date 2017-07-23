import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

#Function to input code from bot and return the response
def grab_general(fccid):
    fccID = fccid
    url = ('http://fccid.io/%s' % fccID)
    fcc_query = urlopen(url)
    content = fcc_query.read(url, user_agent)

    rel = '<h1>FCC ID 2ADUIESP-12</h1>(.*?)</h4>'
    rg = re.compile(rel, re.IGNORECASE | re.DOTALL)
    m = rg.search(content.decode('utf-8'))
    if m:
        general_data = m.group(1)
        print("FCC Holder: (" + general_data + ")" + "\n")

    send_back = general_data
    return send_back

def start(fccid):
    page = requests.get("https://fccid.io/%s" % fccid)
    #print(page.content)
    soup = BeautifulSoup(page.content, "lxml")

    title = soup.findAll("title")
    dev = re.findall("<title>FCC ID " + fccid + ".(.*?)</title>", str(title))


    freqs = soup.findAll("div", { "class" : "panel panel-primary" })
    print(dev)
    #print(soup.prettify())
    #soup = soup.select('<h4>')
    #print(soup)

def dev(fccid):
    page = requests.get("https://fccid.io/%s" % fccid)
    soup = BeautifulSoup(page.content, "lxml")
    title = soup.findAll("title")
    dev = re.findall("<title>FCC ID " + fccid + ".(.*?)</title>", str(title))
    return(dev)

def freq(fccid):
    page = requests.get("https://fccid.io/%s" % fccid)
    soup = BeautifulSoup(page.content, "lxml")
    freqs = soup.findAll("div", {"class": "panel panel-primary"})
    printme = re.findall("lower=(.*?)</a></td><td>",str(freqs))
    printme2 = re.findall(r'>.*?\Z', str(printme[0]))

    print(printme2[0])
    return(printme2[0])


#start('EW780-5735-02')
#freq('EW780-5735-02')
###to do, remove bad char and replace with nice looking shit on print out