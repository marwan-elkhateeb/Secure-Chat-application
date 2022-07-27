# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 13:01:27 2022

@author: Marwan El_khateeb
"""

from socket import * 
from _thread import * 


s = socket((AF_INET), SOCK_STREAM)
HOST = "192.168.1.4"
PORT = 9999
s.bind( ("192.168.1.4", 9999) )
s.listen(50)


sessions = []

def recvThread(c, ad):
    
    while True:
        message = str(ad[1]) + " : " + c.recv(1048).decode('utf-8')
        for session in sessions:
            if session !=c :
                session.send(message.encode('utf-8'))


while True:
    c, ad = s.accept()
    message = "new connection from " + str(ad[1])
    for session in sessions:
        session.send(message.encode('utf-8'))
    sessions.append(c)
    start_new_thread(recvThread, (c, ad))
    
