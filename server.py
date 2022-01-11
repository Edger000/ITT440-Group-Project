import socket
import select
import sys
import threading

"""The first argument AF_INET is the address domain of the 
socket. This is used when we have an Internet Domain with 
any two hosts The second argument is the type of socket. 
SOCK_STREAM means that data or characters are read in 
a continuous flow."""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# checks whether sufficient arguments have been provided
if len(sys.argv) != 3:
    print("Correct usage: $ python <IP address> <port number>")
    exit()

# takes the first argument from command prompt as IP address
IP_address = str(sys.argv[1])

# takes second argument from command prompt as port number
Port = int(sys.argv[2])

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


class hotelfarecal:
    def __init__(self, conn, rt='', s=0, p=0, r=0, t=0, a=1800, name='', PcNumber='', rno=101):
        self.conn = conn
        self.rt = rt
        self.r = r
        self.t = t
        self.p = p
        self.s = s
        self.a = a
        self.name = name
        self.PcNumber = PcNumber
        self.rno = rno

    def inputdata(self):
        self.conn.send("\nEnter your name:<input here>".encode('utf-8'))
        receive = self.conn.recv(2048)
        self.name = receive.decode('utf-8')
        print("received name:", self.name)
        self.conn.send("\nEnter your Pc Number:<input here>".encode('utf-8'))
        receive = self.conn.recv(2048)
        self.PcNumber = receive.decode('utf-8')
        print("received name:", self.PcNumber)
        print("Your room no.:", self.rno, "\n")

    def Plans(self):  # sel1353

        print("We have the following Plans for you:-")
        print("1.  Plan A---->Rm 5 for 2 hour\-")
        print("2.  Plan B---->Rm 10 for 4 hour\-")
        print("3.  Plan C---->Rm 20 for 6 hour\-")
        print("4.  Plan D---->Rm 25 for 8 hour\-")
        x = int(input("Enter Your Choice Please->"))
        n = int(input("For How Many PC Did You Book:"))
        if (x == 1):
            print("you have opted room Plan A")
            self.s = 5 * n
        elif (x == 2):
            print("you have opted room Plan B")
            self.s = 10 * n
        elif (x == 3):
            print("you have opted room Plan C")
            self.s = 20 * n
        elif (x == 4):
            print("you have opted room Plan D")
            self.s = 25 * n
        else:
            print("please choose a Plan")
        print("your room rent is =", self.s, "\n")

    def Cafebill(self):
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
            Enter your choice:<input here>"""
            c = int(input("Enter your choice:"))

            if (c == 1):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 20 * d
            elif (c == 2):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 10 * d
            elif (c == 3):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 90 * d
            elif (c == 4):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 110 * d
            elif (c == 5):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 150 * d
            elif (c == 6):
                break;
            else:
                print("Invalid option")
        print("Total food Cost=RM", self.r, "\n")


    def display(self):
        print("******Cyber Cafe BILL******")
        print("Customer details:")
        print("Customer name:", self.name)
        print("Room no.", self.rno)
        print("Your PC rent is:", self.s)
        print("Your Food bill is:", self.r)

        self.rt = self.s + self.t + self.p + self.r

        print("Your sub total bill is:", self.rt)
        print("Additional Service Charges is", self.a)
        print("Your grandtotal bill is:", self.rt + self.a, "\n")
        self.rno += 1


def clientthread(conn, addr):
    # sends a message to the client whose user object is conn
    # conn.send("Welcome to this chatroom!")
    a = hotelfarecal(conn)
    while True:
        to_print = """
        *****WELCOME TO HEWING HOTEL*****
        1.Enter Customer Data
        2.Calculate Plan Bill
        3.Calculate Food bill
        4.Show total cost
        5.EXIT
        *********************************
        Enter your choice:<input here>"""

        conn.send(to_print.encode('utf-8'))
        try:
            input_anda = conn.recv(2048)

            b = int(input_anda.decode('utf-8'))
            if (b == 1):
                a.inputdata()

            if (b == 2):
                a.Plans()

            if (b == 3):
                a.Cafebill()

            if (b == 4):
                a.display()

            if (b == 5):
                break
        except ValueError:
            conn.send("Invalid number".encode("utf-8"))
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
