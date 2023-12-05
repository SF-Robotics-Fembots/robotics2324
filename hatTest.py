import pygame
import time
import socket

def main(ip_server):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    serverSocket.bind((ip_server, 5000))
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
            if event.type == pygame.JOYHATMOTION:
                print(event)
        x, y = (pygame.joystick.Joystick(0).get_hat(0))
        clientConnected.send((repr(y)).encode())
        print(y)
    
    
        if y == 1:
            clientConnected.send(("a").encode())
            print("a")
        elif y == -1:
            clientConnected.send(("b").encode())
            print("b")
        time.sleep(.5)

if __name__ == "__main__":
    main()