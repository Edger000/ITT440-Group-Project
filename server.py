# Python program to implement server side of chat room. 
import socket 
import select 
import sys 
from thread import *

"""The first argument AF_INET is the address domain of the 
socket. This is used when we have an Internet Domain with 
any two hosts The second argument is the type of socket. 
SOCK_STREAM means that data or characters are read in 
a continuous flow."""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

# checks whether sufficient arguments have been provided  
if len(sys.argv) != 3:  
    print ("Correct usage: $ python <IP address> <port number>") 
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

print ("Waiting for connections...")

""" 
listens for 100 active connections. This number can be 
increased as per convenience. 
"""
server.listen(100) 

list_of_clients = [] 

def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1800,PcNumber='',rno=101):

        print ("\n\n*****WELCOME TO CYBER CAFE*****\n")

        self.rt=rt

        self.r=r

        self.t=t

        self.p=p

        self.s=s
        self.a=a
        self.PcNumber=PcNumber
        self.rno=rno
def display(self):
        print ("******CYBER BILL******")
        print ("Customer details:")
        print ("Customer PC Number:",self.PcNumber)
        print ("Room no.",self.rno)
        print ("Your PC rent is:",self.s)
        print ("Your Food bill is:",self.r)

        self.rt=self.s+self.t+self.p+self.r

        print ("Your sub total bill is:",self.rt)
        print ("Additional Service Charges is",self.a)
        print ("Your grandtotal bill is:",self.rt+self.a,"\n")
        self.rno+=1
 def HourPlan(self):#sel1353

        print ("We have the following Hour Plan for you:-")

        print ("1.  type A---->RM 5 PN\-")

        print ("2.  type B---->rs 10 PN\-")

        print ("3.  type C---->rs 15 PN\-")

        print ("4.  type D---->rs 20 PN\-")

        x=int(input("Enter Your Choice Please->"))


        if(x==1):

            print ("you have opted Plan type A")

            self.s=6000*n

        elif (x==2):

            print ("you have opted Plan type B")

            self.s=5000*n

        elif (x==3):

            print ("you have opted Plan type C")

            self.s=4000*n

        elif (x==4):
            print ("you have opted Plan type D")

            self.s=3000*n

        else:

            print ("please choose a Plan")

        print ("your Plan rent is =",self.s,"\n")

def clientthread(conn, addr): 

	# sends a message to the client whose user object is conn 
	#conn.send("Welcome to this chatroom!") 
    conn.send("Let's chat") 

    while True: 
        try:
            message = conn.recv(2048) 
            if message: 
                
        print("1.Enter Customer Data")
        
        print("2.Calculate Plans")

        print("3.Calculate restaurant bill")

        print("4.Calculate laundry bill")


        print("6.Show total cost")

        print("7.EXIT")

        b=int(input("\nEnter your choice:"))
        if (b==1):
            a.inputdata()

        if (b==2):

            a.roomrent()

        if (b==3):

            a.restaurentbill()

        if (b==4):

            a.laundrybill()

        if (b==5):

            a.gamebill()

        if (b==6):

            a.display()

        if (b==7):

            quit()
        

            else: 
                """message may have no content if the connection 
                is broken, in this case we remove the connection"""
                remove(conn) 
        except: 
            continue

"""Using the below function, we broadcast the message to all 
clients who's object is not the same as the one sending 
the message """
def broadcast(message, connection): 
	for clients in list_of_clients: 
		if clients!=connection: 
			try: 
				clients.send(message) 
			except: 
				clients.close() 

				# if the link is broken, we remove the client 
				remove(clients) 

"""The following function simply removes the object 
from the list that was created at the beginning of 
the program"""
def remove(connection): 
	if connection in list_of_clients: 
		list_of_clients.remove(connection) 

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
	print (addr[0] + " connected") 

	# creates and individual thread for every user 
	# that connects 
	start_new_thread(clientthread,(conn,addr)) 

conn.close() 
server.close() 