import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('192.168.1.100', 5050))

def sendClient():
	print("socket listening")

#clientSocket.sendall("hello")
	data = input("send a message: ")
	data = data.encode()
	clientSocket.sendall(data)

	print(f"Client Send: {data}")
	receiveClient()

def receiveClient():
	while True:	
		data2 = clientSocket.recv(1024)
		data2.decode()
		if not data2:
			break
		print(f"server received {data2}")
sendClient()
#receiveClient()
