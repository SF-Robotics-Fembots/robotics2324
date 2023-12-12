import time, RPi.GPIO as GPIO, socket

#setup for the board and the pins
GPIO.setmode(GPIO.BCM) #set this to the gpio pins
#both GPIO 23 and 24 for the outputs
GPIO.setup(23, GPIO.OUT) #actually pin 16
GPIO.setup(24, GPIO.OUT) #actually pin 18

#set up the socket connection ugh
#bottomside is client
#global server_ip, port will be defined in the threading program
#server_ip = "192.168.1.100"
port = 40000 #is up for debate


def main(server_ip):
    clientsocket = socket(socket.SOCKSTREAM, socket.AF_INET)
    clientsocket.connect((server_ip, port))
    gripper_on = data



main()