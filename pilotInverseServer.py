import pygame
import time
import socket

def main(ip_server):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    print("1")

    serverSocket.bind((ip_server, 7070)) #replace
    print("2")
    serverSocket.listen(1)
    print("socket listening")
    
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    pygame.init()
    
    (clientConnected, clientAddress) = serverSocket.accept()
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.JOYBUTTONDOWN:
                print(event)
        buttonNorm = (pygame.joystick.Joystick(0).get_button(10))
        buttonInv = (pygame.joystick.Joystick(0).get_button(11))
        if(buttonNorm == 1):
            clientConnected.send(("a").encode())
            #print("a")
        elif(buttonInv == 1):
            clientConnected.send(("b").encode())
            #print("b")
        else:
            clientConnected.send(("c").encode())
            #print("c")
        time.sleep(.01)

if __name__ == "__main__":
    main()