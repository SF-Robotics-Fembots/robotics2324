import time, RPi.GPIO as GPIO
import socket
import json

#GPIO.cleanup()
#setup for the board and the pins
GPIO.setmode(GPIO.BCM) #set this to the gpio pins
#both GPIO 20 and 21 for the outputs
#first gripper
front_grip = 21
back_grip = 20
GPIO.setup(front_grip, GPIO.OUT) #actually pin 16
GPIO.setup(back_grip, GPIO.OUT) #actually pin 18

#set up the socket connection ugh
#bottomside is client
#global server_ip, port will be defined in the threading program
#ip_server = "192.168.1.100"
port = 40000 #is up for debate
#ip_server = "127.0.0.1"


def main(ip_server):
    #print("Connecting 1")
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #print("Connecting 2")
    clientsocket.connect((ip_server, port))
    #print("connecting 3")
    print("client connected!!")
    while True: 
        #print("client connected!")
        data = clientsocket.recv(1024)
        data = data.decode()
        print(data)
        database = json.loads(data)
        #print(database)
        #set the GPIO values based on the dictionary values
        GPIO.output(front_grip, database['front'])
        GPIO.output(back_grip, database['back'])

    
    GPIO.cleanup()
        
    


if __name__ == "__main__":
    main()
