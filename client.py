# Name: Daniel Hrebenar
# OSU Email: hrebenad@oregonstate.edu
# Course: CS361 - Software Engineering
# Assignment: Final Project - Microservice
# Due Date: End of Term
# Description: This is the program that will interact with the main service. It will collect a name for a plant from the main server and then send the information to a the 
# back end to retrieve the data. Once it receives the plant data back, it will pass the data to the main program. 

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 4444  # The port used by the server
message = b"A message from CS361"

"""
This is the program that is called in the main service. The main service will ask for input and then pass the input to this 
program. This program will then relay the message to the server which will pass the data back. Pseudocode for the example call could 
be:

def sendMessage(self, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        # send the message
        print(f"Sending {message!r}")
        s.sendall(message)
        # receive the respinse
        data = s.recv(1024)
        s.close()
        return data;

"""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Sending {message!r}")
    s.sendall(message)