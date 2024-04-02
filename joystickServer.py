import pygame
import socket
import time

#global ip_server

def main(ip_server):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(ip_server)

    #ratio for thrust speeds
    ratio = 0.5 #50%
    
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    
    pygame.init()
    
    serverSocket.bind((ip_server, 9090)) #was 9090
    serverSocket.listen(1)
    print("socket listening joystick")
    
    (clientConnected, clientAddress) = serverSocket.accept()
    

    slow_speed = 0

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
        '''dockButton = (pygame.joystick.Joystick(0).get_button(4))
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
                time.sleep(.01)'''
        
        if pygame.joystick.Joystick(0).get_button(6): slow_speed = 0
        if pygame.joystick.Joystick(0).get_button(4): slow_speed = 1

        def calcValue(joyValue):
            if(abs(joyValue) < 0.05):
                return 0
            else:
                return joyValue
            
        def calcVertValue(joyValue):
            if(abs(joyValue) < 0.10):
                return 0
            else:
                return joyValue

        

        x_speed = (pygame.joystick.Joystick(0).get_axis(0))
        calcValue(x_speed) #preemptive deadzone calcs for everybody!
        if slow_speed: x_speed = x_speed*ratio
        clientConnected.send(("x" + repr(x_speed)).encode())
        print("x_speed: " + str(x_speed))
        
        y_speed = (pygame.joystick.Joystick(0).get_axis(1))
        calcValue(y_speed)
        if slow_speed: y_speed = y_speed*ratio
        clientConnected.send(("y" + repr(y_speed)).encode())
        print("y_speed: " + str(y_speed))
       
        r_speed = (pygame.joystick.Joystick(0).get_axis(2))
        calcValue(r_speed)
        if slow_speed: r_speed = r_speed*ratio
        clientConnected.send(("r" + repr(r_speed)).encode())
        print("r_speed: " + str(r_speed))
       
        v_speed = (pygame.joystick.Joystick(0).get_axis(3))
        calcVertValue(v_speed)
        if slow_speed: v_speed = v_speed*ratio
        clientConnected.send(("v" + repr(v_speed)).encode())
        print("v_speed: " + str(v_speed))

        if slow_speed: clientConnected.send("ratio"+ repr(ratio).encode())
        time.sleep(.01)
        
if __name__ == "__main__":
    main()
