#!/usr/bin/python3

from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
from threading import Thread
import tkinter

# used this repo as a reference: https://github.com/sachans/Chat-App (@sachans)

def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZE).decode("utf16")
            msgList.insert(tkinter.END, msg)
        except OSError:
            break

def send(event=None):
    msg = myMsg.get()
    myMsg.set("")
    client_socket.send(bytes(msg, "utf16"))
    if msg == "fuck this I'm out":
        client_socket.close()
        top.quit()

def onClosing(event=None):
    myMsg.set("fuck this I'm out")
    send()

top = tkinter.Tk()
top.title("TCP guessing game feat. chat")

messages_frame = tkinter.Frame(top)
myMsg = tkinter.StringVar()
myMsg.set("")
scrollbar = tkinter.Scrollbar(messages_frame)
msgList = tkinter.Listbox(messages_frame, height = 20, width = 60, yscrollcommand = scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill = tkinter.Y)
msgList.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msgList.pack()
messages_frame.pack()

entryFields = tkinter.Entry(top, textvariable=myMsg)
entryFields.bind("<Return>", send)
entryFields.pack()
sendButton = tkinter.Button(top, text="Put it in", command=send)
sendButton.pack()

top.protocol("WM_DELETE_WINDOW", onClosing)

top.configure(bg="black")

HOST = input("Punch in an IP/URL: ")
PORT = 6969
BUFSIZE = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  
