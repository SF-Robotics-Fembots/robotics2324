import time, socket, sys

print("Initialising....\n")

server = socket.socket()
server.bind(('192.168.1.100', 5050))
           
server.listen(1)
print("\nWaiting for incoming connections...\n")
conn, addr = server.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

server_name = conn.recv(1024)
server_name = server_name.decode()

conn.send(server_name.encode())

count = 0
while True:
    message = input(str("Send message : "))
    count+=1
    if count == 10:
        message = "Connection closed"
        conn.send(message.encode())
        print("\n")
        break
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print("response: ", message)
