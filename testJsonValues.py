#works w/ sockets
#library for r
import pygame   #pip install pygame
import board	#pip install board
import busio	#pip install adafruit-blinka
#used for 12C abstractions
#abstractions: gives names to things, so the name captures the core of what the function/program does
#used for input and output
#module in python
import adafruit_pca9685 #pip install adafruit-circuitpython-pca9685
#controls servos and PWM (pulse width module)
#controls servos and pwm
#pca9685 controls pwm chip in shield
#adafruit: circuit playground allowing simple data connections
from adafruit_servokit import ServoKit #pip install adafruit-circuitpython-servokit
import time
#hz, ms, etc.
import socket, json
#socket: one andpoint of a two-way communication link btwn two programs running the network

#MOD: from array import array
ip_server = "192.168.1.103"
def main():
	# library setup
	pygame.init()

	#setting up the median of the 'off' values for the thrusters
	horiz_off_value = 1500
	horiz_thrust_offset = 60
	vert_off_value = 1484
	vert_thrust_offset = 25

	#debug! make more laters
	debug_l2 = 0

	#rotation compensation
	rot_comp = -0.08

	i2c = busio.I2C(board.SCL, board.SDA)
	#SCL: serial clock number
	#SDA: serial data line
	#needed to pulse high and low to send and receive data
	shield = adafruit_pca9685.PCA9685(i2c)
	#shield: drives pwm for each thruster
	kit = ServoKit(channels=16)
	#servo kit for adafruit
	#channels: models for interprocess communication and synchronization via message passing
	shield.frequency = 96

	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#SOCK_STREAM: socket type for TCP
	#TCP: Transmission Control Protocol
	#TCP: communications standard that enables application programs and computing devices to exchange messages over a network
	clientSocket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#AF_INET: internet address family for IPv4
	#IPv4: network protocol and transmission
# 192.169.1.100 is comp computer ip
	clientSocket.connect((ip_server, 9090))
	clientSocket1.connect((ip_server, 7070))
        
	
	#everytime data is sent, previous values are set to 0 (updates & loops values)

#MOD: prevValue = array[prevX, prevY, prevV, prevR]
#MOD: prevValue = 0

#MOD: value_speed = array[x_speed, y_speed, v_speed, r_speed]
#input this in the while TRue function
	# main loop
	while True:
		try:
			dataFraud = (clientSocket.recv(1024)).decode()
			print("dataFraud type: " + str(type(dataFraud)))

			thrusterMovements = json.loads(dataFraud)
			print("thruster movement dict: " + str(thrusterMovements))
			print("thruster movement type: " + str(type(thrusterMovements)))
			time.sleep(3)
			if debug_l2: print("datafraud: " + dataFraud)
			data = (clientSocket.recv(1024)).decode()
			if debug_l2: print("data " + data)
			#power calculations
			time.sleep(2)

		except ValueError:
			print("Error")
			check = (clientSocket.recv(1024)).decode()
			print("check: " + check)
			print("dataFraud: " + dataFraud)
			time.sleep(2)

if __name__ == "__main__":
    main()
