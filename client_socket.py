#!/usr/bin/python3
"""create a client socket"""
import socket


def client_socket():
    """The client socket"""
    host = socket.gethostname()
    port = 5004

    client_s = socket.socket() #instance of socket
    client_s.connect((host, port)) #make connection

    message = input('->') #default message

    while message.lower().strip() != 'bye':
        client_s.send(message.encode()) #send message
        data = client_s.recv(1024).decode() #decode received message
        print("Received from server: {}".format(str(data)))
        message = input('->')
    client_s.close()

if __name__ == "__main__":
    client_socket()
