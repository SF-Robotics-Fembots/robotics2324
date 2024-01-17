import time, RPi.GPIO as GPIO
import socket

GPIO.cleanup()
#setup for the board and the pins
GPIO.setmode(GPIO.BCM) #set this to the gpio pins
#both GPIO 23 and 24 for the outputs
GPIO.setup(26, GPIO.OUT) #actually pin 16
GPIO.setup(13, GPIO.OUT) #actually pin 18

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
    while True: 
        print("client connected!")
        data = clientsocket.recv(1024)
        data = data.decode()
        print(data)
        if data == "a":
            GPIO.output(26, GPIO.HIGH) #turns the gripper on
            GPIO.output(13, GPIO.HIGH)
            print(data)
            time.sleep(1.5)
        elif data == "b":
            GPIO.output(26, GPIO.HIGH)
            GPIO.output(13, GPIO.HIGH)
            print(data)
            time.sleep(1)
    
    GPIO.cleanup()
        
    



main()
