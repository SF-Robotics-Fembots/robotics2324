# EXCEPTION TEST 

import lgpio
import pygame
import board
import busio
import adafruit_pca9685
from adafruit_servokit import ServoKit
import time
import socket
import array

def main():
	pygame.init()

	i2c = busio.I2C(board.SCL, board.SDA)
	shield = adafruit_pca9685.PCA9685(i2c)
	kit = ServoKit(channels=16)
	shield.frequency = 100

	thrusterChannel = array[shield.channels[0], shield.channels[1], shield.channels[2], shield.channels[3], shield.channels[4], shield.channels[5], shield.channels[6]]
	
	throttle_in = 1480
	throttlePW = int(throttle_in/10000*65536)
	thrusterChannel.duty_cycle = throttlePW
	time.sleep(0)

	throttle_in = 2200
	throttlePW = int(throttle_in/10000*65536)
	thrusterChannel.duty_cycle = throttlePW
	time.sleep(0)

	def calcHorizontalandVert(joyValue, thrusterNum, direction):
		if (-5 <= joyValue <= 5):        
			return 0
		else:
			joyValue = joyValue - ((abs(joyValue)/joyValue) * 5)
			return joyValue * direction[thrusterNum]

	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientSocket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientSocket.connect(("192.168.1.100", 9090))
	clientSocket1.connect(("192.168.1.100", 7070))
        
	prevValue = 0

	directionRecieved = "a"
	direction = 1
	while True:
		try:
			dataFraud = (clientSocket.recv(1024)).decode()
			data = (clientSocket.recv(1024)).decode()

			x_speed = dataFraud

			y_speed = data[data.find('y'):data.find('r')]

			r_speed = data[data.find('r'):data.find('v')]

			v_speed = data[data.find('v'):data.find('x')]

			value_speed = value_speed[1:]
			value_speed = float(value_speed)

			value_speed = array[x_speed, y_speed, r_speed, v_speed]
			diffValue = value_speed - prevValue

			if(abs(diffValue) > 0.05):
				value_speed = prevValue + ((diffValue/abs(diffValue)) * 0.10)

			prevValue = value_speed
			prevR = r_speed

			value_speed = int((value_speed)*50)
			prevR = int((r_speed)*25)
			
			directionRecieved = ((clientSocket1.recv(1024)).decode())
			directionRecieved = directionRecieved[0]

			if (directionRecieved == "a"):
			    direction = 1
			elif (directionRecieved == "b"):
			    direction = -1
			else:
			    direction = direction
			print(directionRecieved)
			print(direction)
			xDirArray = [-1*direction, 1*direction, -1*direction, 1*direction]
			yDirArray = [1*direction, 1*direction, -1*direction, -1*direction]
			rDirArray = [-1, 1, 1, -1]
			vDirArray = [-1, -1]

			thrusterVals = [0, 0, 0, 0]
			vertThrusterVals = [0, 0]

			for tNum in range(0,4):
				thrusterVals[tNum] = int((calcHorizontalandVert(x_speed, tNum, xDirArray) + calcHorizontalandVert(y_speed, tNum, yDirArray) + calcHorizontalandVert(r_speed, tNum, rDirArray)))
			for vNum in range(0,2):
				vertThrusterVals[vNum] = int((calcHorizontalandVert(v_speed, vNum, vDirArray)))

			max_thruster = 0
			for thrusters in range(0,4):
				max_thruster = max(max_thruster, abs(thrusterVals[thrusters]))

			if (max_thruster != 0) and (max_thruster >= 50):
				for thrusters in range(0, 4):
					thrusterVals[thrusters] = int(thrusterVals[thrusters] * (50 / max_thruster))


			powerThrusterVals = [0, 0, 0, 0]
			powerVertThrusterVals = [0, 0]

			for thrusters in range(0, 4):
				if (thrusterVals[thrusters] == 0):
					powerThrusterVals[thrusters] = 1489
				else:
					powerThrusterVals[thrusters] = 1489 + ((abs(thrusterVals[thrusters])/thrusterVals[thrusters]) * 25) + (thrusterVals[thrusters] * 7.0)
			for vertThrusters in range(0, 2):
				if (vertThrusterVals[vertThrusters] == 0):
					powerVertThrusterVals[vertThrusters] = 1489
				else:
					powerVertThrusterVals[vertThrusters] = 1489 + ((abs(vertThrusterVals[vertThrusters])/vertThrusterVals[vertThrusters]) * 25) + (vertThrusterVals[vertThrusters] * 7.0)

			finalHorDiff = abs(powerThrusterVals[1] - 1489)
			finalVertDiff = abs(powerVertThrusterVals[1] - 1489)
			finalTotal = (finalHorDiff * 4) + (finalVertDiff * 2)
			if (finalTotal != 0):
				percent = (1950/finalTotal)
				if (finalTotal > 1950): 
					for thruster in range(0, 4):
						Diff = powerThrusterVals[thruster] - 1489
						newDiff = Diff * (percent)
						powerThrusterVals[thruster] = 1489 + newDiff
					for vertThruster in range(0, 2):
						vertDiff = powerVertThrusterVals[vertThruster] - 1489
						newVertDiff = vertDiff * (percent)
						powerVertThrusterVals[vertThruster] = 1489 + newVertDiff

			print(powerThrusterVals)

			throttlePW = int(powerThrusterVals[0, 1, 2, 3]/10000*65536)
			thrusterChannel.duty_cycle = throttlePW

			throttlePW = int(powerVertThrusterVals[0, 1]/10000*65536)
			thrusterChannel.duty_cycle = throttlePW

		except ValueError:
			print("Error")
			check = (clientSocket.recv(1024)).decode()
			print("check: " + check)

if __name__ == "__main__":
    main()
