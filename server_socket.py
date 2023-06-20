#!/usr/bin/python3
"""create a server socket"""
import socket


def server_socket():
    """The server socket"""
    host = socket.gethostname()
    port = 5004

    server_s = socket.socket() # new socket instance
    server_s.bind((host, port)) # bind socekt to address and port

    server_s.listen(2)
    # server_S.accept() returns new socket to send and receive
    # on the connection and an address bound to client socket
    (clientsocket, address) = server_s.accept()
    print("Connection from: {}".format(str(address)))
    while True:
        data = clientsocket.recv(1024).decode()
        if not data:
            break
        print("From connected user: {}".format(str(data)))
        data = input('->')
        clientsocket.send(data.encode())
    clientsocket.close()

if __name__ == "__main__":
    server_socket()
