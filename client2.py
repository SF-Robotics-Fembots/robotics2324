# client.py
import time, socket, sys

print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#shost = socket.gethostname()
#ip = socket.gethostbyname(shost)
#print(shost, "(", ip, ")\n")
host = "192.168.1.100"
name = "kin"
port = 5050
#print("\nTrying to connect to ", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port))
print("Connected...\n")

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room\nEnter [e] to exit chat room\n")
count = 0

while True:
    message = s.recv(1024)
    message = message.decode()
    print("message: ", message)
    time.sleep(1)
    message2 = "hi"
    if count == 10:
        message = "Left chat room!"
        s.send(message2.encode())
        print("\n")
        break
    s.send(message2.encode())
    count+=1


#import socket

#clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#clientSocket.connect(('192.168.1.100', 5050))

#def sendClient():
	#print("socket listening")

#clientSocket.sendall("hello")
	#data = input("send a message: ")
	#data = data.encode()
	#clientSocket.sendall(data)

	#print(f"Client Send: {data}")
	#receiveClient()

'''def receiveClient():
	while True:	
		data2 = clientSocket.recv(1024)
		data2.decode()
		if not data2:
			break
		print(f"server received {data2}")
sendClient()'''
#receiveClient()
