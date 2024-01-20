import time, RPi.GPIO as GPIO
import socket

#GPIO.cleanup()
#setup for the board and the pins
GPIO.setmode(GPIO.BCM) #set this to the gpio pins
#both GPIO 20 and 21 for the outputs
GPIO.setup(20, GPIO.OUT) #actually pin 16
GPIO.setup(21, GPIO.OUT) #actually pin 18

#set up the socket connection ugh
#bottomside is client
#global server_ip, port will be defined in the threading program
server_ip = "192.168.1.100"
port = 40000 #is up for debate
#ip_server = "127.0.0.1"


def main():
    #print("Connecting 1")
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #print("Connecting 2")
    clientsocket.connect((server_ip, port))
    #print("connecting 3")
    print("client connected!!")
    while True: 
        #print("client connected!")
        data = clientsocket.recv(1024)
        data = data.decode()
        #print(data)
        if data == "a":
            GPIO.output(20, GPIO.HIGH) #turns the gripper on
            GPIO.output(21, GPIO.HIGH)
            print("gripper on")
            time.sleep(1.5)
        elif data == "b":
            GPIO.output(20, GPIO.LOW)
            GPIO.output(21, GPIO.LOW)
            print("gripper off")
            time.sleep(1.5)
    
    GPIO.cleanup()
        
    



main()
