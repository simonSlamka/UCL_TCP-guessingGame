'''
Exercise instructions
Requirements for the number guessing game are:

On game start calculate a random number between 0 and 9
The computer will give you 3 attempts to guess the number, otherwise the computer wins the round
If the user enters anything else than a number print the message Thats not even a number.... restarting and then restart the program
If the user wins print Damn, you won!, try again? (y/n)
If the computer wins, print na na I won :-P - try again? (y/n)
If user enters y at the end of a round, restart the program
If the user enters n at the end of a round, print the total rounds score between human and computer
'''

# used this repo as a reference: https://github.com/sachans/Chat-App (@sachans)

#!/usr/bin/python3

from random import randint
from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
from threading import Thread
from random import randint

def acceptConnection():
    while True:
        client, client_addr = srv.accept()
        print("Someone has just jacked in!")
        client.send(bytes("Hello, kind stranger! Now I got your IP and personal details, idiot!", "utf16"))
        addresses[client] = client_addr
        Thread(target=handleClient, args=(client,)).start()

def handleClient(client):
    name = client.recv(BUFSIZE).decode("utf16")
    client.send(bytes("Now you're in!", "utf16"))
    broadcast(bytes("Intruder alert!!!", "utf16"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZE)
        if msg != bytes("fuck this I'm out", "utf16"):
            broadcast(msg, name + ":: ")
        elif msg == bytes("gimme a number", "utf16"):
            randInt = randint(1, 99999)
            broadcast("I got you a number, idiots!")
            broadcast(randInt)
        else:
            client.send(bytes("fuck this I'm out", "utf16"))
            client.close()
            del clients[client]
            broadcast(bytes("Someone has just left! Fucker!!", "utf16"))
            break

def broadcast(msg, prefix=""):
    for sock in clients:
        sock.send(bytes(prefix, "utf16")+msg)

clients = {}
addresses = {}

HOST = ''
PORT = 6969
BUFSIZE = 1024
ADDR = (HOST, PORT)

srv = socket(AF_INET, SOCK_STREAM)
srv.bind(ADDR)

srv.listen(10)
print("Waiting for someone to fckin join the party! 🥳")
ACCEPT_THREAD = Thread(target=acceptConnection)
ACCEPT_THREAD.start()
ACCEPT_THREAD.join()
srv.close()
