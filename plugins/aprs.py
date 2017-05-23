#!/usr/bin/env python

import socket
import sys

Server = 'second.aprs.net'
Port = 20157
Buffer_Size = 1024
Con_MSG = 'user KR0SIV pass 16821 ver \"Discord_Bridge\"\n'
Message ='KR0SIV>APRS,TCPIP*:=4148.19N/08056.81W- Discord Test Python Server Dev\n'



def sendmsg(aprs_call, aprs_tocall, aprs_passcode, aprs_message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('==>Created socket successfully\n')
    s.connect((Server, Port))
    conn_msg = 'user ' + aprs_call.upper() + ' pass ' + aprs_passcode + '\n'
    tosend = conn_msg + '\n'
    s.send(tosend.encode('utf-8'))
    print("==>sent " + conn_msg)

    send_aprsmsg = aprs_call + '>APDR12,ACTV8M,WIDE1*,qAR,VE3CRC::' + aprs_tocall.upper() + '    :' + aprs_message
    socketcommand = send_aprsmsg + '\n'
    s.send(socketcommand.encode('utf-8'))

    data = s.recv(2024)
    print("==> " + data.decode('utf-8'))
    #RX_Sock()
    s.close()
    return data.decode('utf-8')

def RX_Sock():
    while True:
        data = s.recv(1024)
        print("==>Recieved " + data.decode('utf-8'))


#run_aprs()
#sendmsg('kr0siv', 'wb5od', '16821', 'this is a message')