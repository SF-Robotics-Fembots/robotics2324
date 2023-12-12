#import time, RPi.GPIO as GPIO
import socket, time

#setup for the board and the pins
#GPIO.setmode(GPIO.BCM) #set this to the gpio pins
#both GPIO 23 and 24 for the outputs
#GPIO.setup(23, GPIO.OUT) #actually pin 16
#GPIO.setup(24, GPIO.OUT) #actually pin 18

#set up the socket connection ugh
#bottomside is client
#global server_ip, port will be defined in the threading program
#server_ip = "192.168.1.100"
port = 40000 #is up for debate
ip_server = "127.0.0.1"


def main():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((ip_server, port))
    while True: 
        print("client connected!")
        data = clientsocket.recv(1024)
        data = data.decode()
        print(data)

        time.sleep(1.5)
        break
    print("socket closing!")
    clientsocket.close()
        
    



main()