import dataclasses
import socket
import select
import sys
import threading
import time

"""The first argument AF_INET is the address domain of the 
socket. This is used when we have an Internet Domain with 
any two hosts The second argument is the type of socket.    
SOCK_STREAM means that data or characters are read in 
a continuous flow."""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# takes the first argument from command prompt as IP address
IP_address = "localhost"

# takes second argument from command prompt as port number
Port = 6000

""" 
binds the server to an entered IP address and at the 
specified port number. 
The client must be aware of these parameters 
"""
server.bind((IP_address, Port))

print("Waiting for connections...")

""" 
listens for 100 active connections. This number can be 
increased as per convenience. nerd
"""
server.listen(100)

list_of_clients = []


class CyberCafe:
    def __init__(self):
        self.occupied_pc = []
        self.available_pc = [1001, 1002, 1003, 1004, 1005]

    def input_data(self, client):
        client.name = client.input("\nEnter your name:")
        pc_avail = ""
        for pc_no in self.available_pc:
            pc_avail += f"PC NO: {pc_no}\n"

        client.pc = int(client.input(f"{pc_avail}\nEnter your Pc Number:"))
        self.occupied_pc.append(client.pc)
        self.available_pc.remove(client.pc)
    
    def membership(self, client):
        while True:
            n = client.input("Do you have membership? Member will get 10& discount(y/n)")
            val = n.lower()
            if val in ('yes', 'y'):
                return True
            elif val in ('no', 'n'):
                return False
            else:
                client.send("Invalid Response, please respond (y) for Yes or (n) for No")

    def discount(self, client):
        while True:
            n = client.input("Do you want to double your plan for a 10% discount?(y/n)")
            val = n.lower()
            if val in ('yes', 'y'):
                return True
            elif val in ('no', 'n'):
                return False
            else:
                client.send("Invalid Response, please respond (y) for Yes or (n) for No")

    def plans(self, client):
        to_print = """We have the following Plans for you:-
        1.  Plan A---->Rm 5 for 2 hour\-
        2.  Plan B---->Rm 10 for 5 hour\-
        3.  Plan C---->Rm 20 for 7 hour\-
        4.  Plan D---->Rm 25 for 9 hour\-
        
        Enter Your Choice Please->"""
        while True:
            try:
                x = int(client.input(to_print))
                if (x == 1):
                    client.send("you have opted room Plan A")
                    client.plan = 5
                elif (x == 2):
                    client.send("you have opted room Plan B")
                    client.plan = 10
                elif (x == 3):
                    client.send("you have opted room Plan C")
                    client.plan = 20
                elif (x == 4):
                    client.send("you have opted room Plan D")
                    client.plan = 25
                else:
                    client.send("please choose a Plan")
                    continue
                break
            except ValueError:
                client.send("Invalid number")

        has_discount = self.discount(client)
        has_membership = self.membership(client)
        if has_discount:
            client.plan *= 2 - client.plan * 0.1
            client.time *= 2

        client.time = datetime.datetime.now() + datetime.timedelta(hours=client.time)

        if has_membership:
            client.plan -= client.plan * 0.1

        client.send(f"Your total payment for your plan is RM{client.plan}\n")

    def timer(self, client):
        t = client.plans()
        while t:
        hours = t // 3600
        mins = t // 60
        secs = t % 3600
        timer = '{:02d}:{02d}:{02d}'.format(hours, mins, secs)
        print(timer, end="\r")
        t -= 1
        print('Time Up!!')
    
    def addTime(self,client)
        while True:
            n = client.input("Your time is up! Do you wish to add more time? please respond (y) for Yes or (n) for No")
            val = n.lower()
            if val in ('yes', 'y'):
                if val in ('yes', 'y'):
                to_print = """We have the following add options for you:-
                1.  A---->Rm 5 for 3 hour\-
                2.  B---->Rm 10 for 6 hour\-
                3.  C---->Rm 20 for 8 hour\-
                4.  D---->Rm 25 for 10 hour\-
        
                Enter Your Choice Please->"""
                while True:
                    try:
                        x = int(client.input(to_print))
                        if (x == 1):
                            client.send("you have opted room Plan A")
                            client.plan = 5
                        elif (x == 2):
                            client.send("you have opted room Plan B")
                            client.plan = 10
                        elif (x == 3):
                            client.send("you have opted room Plan C")
                            client.plan = 20
                        elif (x == 4):
                            client.send("you have opted room Plan D")
                            client.plan = 25
                        else:
                            client.send("please choose a Plan")
                            continue
                        break
                    except ValueError:
                        client.send("Invalid number")
                    elif val in ('no', 'n'):
                        return False
                    else:
                        client.send("Invalid Response, please respond (y) for Yes or (n) for No")
            elif val in ('no', 'n'):
                return False
            else:
                client.send("Invalid Response, please respond (y) for Yes or (n) for No")

    def cafe_bill(self, client):
        price = None
        while True:
            to_print = """
            *****Cyber Cafe Menu*****
            1.water----->RM20
            2.tea----->RM10
            3.breakfast combo--->RM90
            4.lunch---->RM110
            5.dinner--->RM150
            6.Exit
            *********************************
            Enter your choice:"""
            c = int(client.input(to_print))
            if (c == 1):
                price = 20
            elif (c == 2):
                price = 10
            elif (c == 3):
                price = 90
            elif (c == 4):
                price = 110
            elif (c == 5):
                price = 150
            elif (c == 6):
                return
            else:
                client.send("Invalid option")
                continue
            break

        while True:
            try:
                q = int(client.input("Enter the quantity:"))
            except ValueError:
                client.send("Invalid number")
            else:
                client.cafe_bill = price * q
                client.send(f"Total food Cost=RM{client.cafe_bill}\n")
                break

    def display(self, client):
        client.send("******Cyber Cafe BILL******\n")
        client.send("Customer details:\n")
        client.send("Customer name:", client.name, "\n")
        client.send("Room no.", client.pc, "\n")
        client.send("Your PC rent is:", client.plan, "\n")
        client.send("Your Food bill is:", client.cafe_bill, "\n")
        client.send("Your grandtotal bill is:", client.total(), "\n")


class Client:
    def __init__(self, conn: socket.socket, pc: int, name: str) -> None:
        self.conn = conn
        self.pc = pc
        self.name = name
        self.cafe_bill = 0
        self.plan = 0

    def input(self, *send):
        to_send = " ".join(map(str, send)) + "<input here>"
        self.send(to_send)
        return self.conn.recv(2048).decode('utf-8')

    def send(self, *to_send):
        formatted = " ".join(map(str, to_send))
        print("Sending to ", conn.getsockname(), ":", formatted)
        self.conn.send(formatted.encode('utf-8'))

    def total(self):
        return self.plan + self.cafe_bill


cyber = CyberCafe()


def clientthread(conn, addr):
    # sends a message to the client whose user object is conn
    # conn.send("Welcome to this chatroom!")
    client = Client(conn, 0, "")
    while True:
        to_print = """
        *****WELCOME TO HEWING cyber*****
        1.Enter Customer Data
        2.Calculate Plan Bill
        3.Calculate Food bill
        4.Show total cost
        5.EXIT
        *********************************
        Enter your choice:"""

        try:
            input_anda = client.input(to_print)
            b = int(input_anda)
            if (b == 1):
                cyber.input_data(client)

            if (b == 2):
                cyber.plans(client)

            if (b == 3):
                cyber.cafe_bill(client)

            if (b == 4):
                cyber.display(client)

            if (b == 5):
                break
        except ValueError:
            client.send("Invalid number")
    conn.close()


while True:
    """Accepts a connection request and stores two parameters, 
    conn which is a socket object for that user, and addr 
    which contains the IP address of the client that just 
    connected"""
    conn, addr = server.accept()

    """Maintains a list of clients for ease of broadcasting 
    a message to all available people in the chatroom"""
    list_of_clients.append(conn)

    # prints the address of the user that just connected
    print(addr[0] + " connected")

    # creates and individual thread for every user
    # that connects
    to_start = threading.Thread(target=clientthread, args=(conn, addr))
    to_start.start()
