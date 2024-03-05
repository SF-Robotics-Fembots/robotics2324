import pygame
import socket
import time

#global ip_server

def main(ip_server):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(ip_server)
    
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    
    pygame.init()
    
    serverSocket.bind((ip_server, 9090)) #was 9090
    serverSocket.listen(1)
    print("socket listening joystick")
    
    (clientConnected, clientAddress) = serverSocket.accept()
    
    while True:
        print("joystick loop")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.JOYAXISMOTION:
                print(event)
            if event.type == pygame.JOYBUTTONDOWN:
                print(event)
    
    # collect joystick values as -1 to 1
        dockButton = (pygame.joystick.Joystick(0).get_button(4))
        if(dockButton == 1):
            num = 400
            for _ in range(num):
                xDir = "x0.0"
                clientConnected.send(xDir.encode())
                yDir = "y-0.3"
                clientConnected.send(yDir.encode())
                rDir = "r0.0"
                clientConnected.send(rDir.encode())
                vDir = "v0.0"
                clientConnected.send(vDir.encode())
                time.sleep(.01)

        x_speed = (pygame.joystick.Joystick(0).get_axis(0))
        clientConnected.send(("x" + repr(x_speed)).encode())
        print("x_speed: " + str(x_speed))
        #time.sleep(5)
        y_speed = (pygame.joystick.Joystick(0).get_axis(1))
        clientConnected.send(("y" + repr(y_speed)).encode())
        print("y_speed: " + str(y_speed))
        #time.sleep(5)
        r_speed = (pygame.joystick.Joystick(0).get_axis(2))
        clientConnected.send(("r" + repr(r_speed)).encode())
        print("r_speed: " + str(r_speed))
        #time.sleep(5)
        v_speed = (pygame.joystick.Joystick(0).get_axis(3))
        clientConnected.send(("v" + repr(v_speed)).encode())
        print("v_speed: " + str(v_speed))
        time.sleep(.01)
        
if __name__ == "__main__":
    main()