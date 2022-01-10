
import socket
import select
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()

IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
client.connect((IP_address, Port))

def receive():
    return client.recv(2048).decode('utf-8')


while True:
    value = receive()
    if value.endswith("<input here>"):
        cleared = value.rstrip("<input here>")
        client.send(input(cleared).encode('utf-8'))
    else:
        print(value)
