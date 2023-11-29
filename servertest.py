import socket

#initializes server socket and binds to ip and port number
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(1)
serverSocket.bind(('192.168.1.100', 5050))
print(2)
serverSocket.listen(0)
print("socket listening")

conn, addr = serverSocket.accept()

print("socket.accepted")

def receiveServer():
    

    with conn:
        print("connected")
        while True:
            data = conn.recv(1024)
            data.decode()
            if not data:
                break
            print(f"server received: {data}")

            sendBack()

            

def sendBack():
    print(1)
    with conn:
        message2 = input("you did it! now send something back!: ")

        message2 = message2.encode()
        serverSocket.send(message2)

int = 0

print(int)
receiveServer()

#sendBack()
