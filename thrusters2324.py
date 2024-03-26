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
import socket
#socket: one andpoint of a two-way communication link btwn two programs running the network

#MOD: from array import array

def main(ip_server):
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
	rot_comp = 0.1

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
	#changed the shield frequency (pwm) to 96 Hz
	#100 in Hz, meaning shield runs at 100 times a second
	#100 Hz = cycle time for PWM signal
	#meaning robot speed can change 100 times a second

	thrusterChannel1 = shield.channels[14]
	thrusterChannel2 = shield.channels[15]
	thrusterChannel3 = shield.channels[2]
	thrusterChannel4 = shield.channels[13] #changed from 3, 4, 5
	thrusterChannel5 = shield.channels[0]
	thrusterChannel6 = shield.channels[1]
	thrusterChannel1.duty_cycle = 0x2666
	#duty cycle: ration of PW to range (tells power of thrusters/how fast thrusters go)
	#NOTE: cycle time for PWM doesnt change, but duty cycle does
	#NOTE: pwm wire = signal connection to thrusters
	#0x2666: sets range for power of duty cycle
#MOD: change to thrusterchannel = array[shield.channels[0], shield.channels[1], shield.channels[2], shield.channels[3], shield.channels[4], shield.channels[5]]

	throttle_in = 2200
	throttlePW = int(throttle_in/10000*65536)
	thrusterChannel1.duty_cycle = throttlePW
	time.sleep(0)

	throttle_in = 1480
	throttlePW = int(throttle_in/10000*65536)
	thrusterChannel1.duty_cycle = throttlePW
	time.sleep(0)

	throttle_in = 2200
	throttlePW = int(throttle_in/10000*65536)
	thrusterChannel2.duty_cycle = throttlePW
	time.sleep(0)

	throttle_in = 1480
	throttlePW = int(throttle_in/10000*65536)
	thrusterChannel2.duty_cycle = throttlePW
	time.sleep(0)

	throttle_in = 2200
	throttlePW = int(throttle_in/10000*65536)
	thrusterChannel3.duty_cycle = throttlePW
	time.sleep(0 )

	throttle_in = 1480
	throttlePW = int(throttle_in/10000*65536)
	thrusterChannel3.duty_cycle = throttlePW
	time.sleep(0)

	throttle_in = 2200
	throttlePW = int(throttle_in/10000*65536)
	thrusterChannel4.duty_cycle = throttlePW
	time.sleep(0)

	throttle_in = 1480
	throttlePW = int(throttle_in/10000*65536)
	thrusterChannel4.duty_cycle = throttlePW
	time.sleep(0)

	throttle_in = 2200
	throttlePW = int(throttle_in/10000*65536)
	thrusterChannel5.duty_cycle = throttlePW
	time.sleep(0)

	throttle_in = 1480
	throttlePW = int(throttle_in/10000*65536)
	thrusterChannel5.duty_cycle = throttlePW
	time.sleep(0)

	throttle_in = 2200
	throttlePW = int(throttle_in/10000*65536)
	thrusterChannel6.duty_cycle = throttlePW
	time.sleep(0)

	throttle_in = 1480
	throttlePW = int(throttle_in/10000*65536)
	thrusterChannel6.duty_cycle = throttlePW
	time.sleep(0)
	#lines 52-110: setting throttle values
#MOD: throttle_in = 2200
# throttlePW = int(throttle_in/10000*65536)
# thrusterchannel.duty_cycle = throttlePW
# time.sleep(0)

#MOD: throttle_in = 1480
# throttlePW = int(throttle_in/10000*65536)
# thrusterchannel.duty_cycle = throttlePW
# time.sleep(0)

#MOD: calcDir = array[horizontal, vertical]

	#horizontal thrusters calculations
	def calcHorizontal(joyValue, thrusterNum, direction):
		if (-5 <= joyValue <= 5):         # can adjust to create deadzone
			return 0
		#used to be 5 on both horizontal and vertical deadzones
		#creates deadzones for where the joystick values do not do anything
		#calculation for everything but 0
		else:
			joyValue = joyValue - ((abs(joyValue)/joyValue) * 5)
			#abs = absolute value, so abs(joy(value)) will always be positive
			return joyValue * direction[thrusterNum]
			#return (((1/750) * ((abs(joyValue))**2.5)) * ((abs(joyValue))/(joyValue)) * direction[thrusterNum])

	# vertical thrusters calculations
	def calcVertical(joyValue, thrusterNum, direction):
		if (-10 <= joyValue <= 10):
			return 0
		# calculation for everything not 0
		else:
			joyValue = joyValue - ((abs(joyValue)/joyValue) * 5)
			return joyValue * direction[thrusterNum]
			#return (((1/750) * ((abs(joyValue))**2.5)) * ((abs(joyValue))/(joyValue)) * direction[thrusterNum]) #was 1000
			#vertical values change if joystick values are btwn -5 and 5

			#lines 115-123: calculates vertical and horizontal power values for joystick values that are not in the deadzone

#MOD: change calcVertical & calcHorizontal to caclDir
#MOD: delete def calcVeritical

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
        
	prevX = 0
	prevY = 0
	prevV = 0
	prevR = 0
	#everytime data is sent, previous values are set to 0 (updates & loops values)

#MOD: prevValue = array[prevX, prevY, prevV, prevR]
#MOD: prevValue = 0

#MOD: value_speed = array[x_speed, y_speed, v_speed, r_speed]
#input this in the while TRue function

	directionRecieved = "a"
	direction = 1
	# main loop
	while True:
		try:
			dataFraud = (clientSocket.recv(1024)).decode()
			#time.sleep(1)
			if debug_l2: print("datafraud: " + dataFraud)
			data = (clientSocket.recv(1024)).decode()
			if debug_l2: print("data " + data)

			x_speed = dataFraud
			x_speed = x_speed[1:]
			#[1:]: used for inverse orders/directions
			x_speed = float(x_speed)
	
			y_speed = data[data.find('y'):data.find('r')]
			y_speed = y_speed[1:]
			y_speed = float(y_speed)
			
			r_speed = data[data.find('r'):data.find('v')]
			r_speed = r_speed[1:]
			r_speed = float(r_speed)
			
			v_speed = data[data.find('v'):data.find('x')]
			v_speed = v_speed[1:]
			v_speed = float(v_speed)
			

			#lines 157-190: translates first measured joystick values, which comes as a float, from top side
			#then, the float goes through a char*
			#the float is translated through the char* (via parsing) into another float that the top computer can understand&receive

			diffX = x_speed - prevX
			diffY = y_speed - prevY
			diffR = r_speed - prevR
			diffV = v_speed - prevV
			#finding difference of speeds to evaluate which ones need power limiting 
			#values used in next if statement

#MOD: diffValue = value_speed - prevValue

			if (abs(diffX) > 0.05):
				x_speed = prevX + ((diffX/abs(diffX)) * 0.10)
			if (abs(diffY) > 0.05):
				y_speed = prevY + ((diffY/abs(diffY)) * 0.10)
			if (abs(diffR) > 0.05):
				r_speed = prevR + ((diffR/abs(diffR)) * 0.10)
			if (abs(diffV) > 0.05):
				v_speed = prevV + ((diffV/abs(diffV)) * 0.10)
				#helps manage power
				#if diffvalue is greater than .05, then it will assign speed a lower values by multiplying diffValue by .1

#MOD: if(abs(diffValue) > 0.05):
		#value_speed = prevValue + ((diffValue/abs(diffValue)) * 0.10)

			prevX = x_speed
			prevY = y_speed
			prevR = r_speed
			prevV = v_speed

#MOD: prevValue = value_speed

			# multiplies original values by 100 (necessary for calculations)
			x_speed = int((x_speed)*50)
			y_speed = int((y_speed)*50)
			r_speed = int((r_speed)*25)
			v_speed = int((v_speed)*50)

			print("R Speed: " + r_speed)
			#rotation compensation :(
			r_speed = int(rot_comp * y_speed + r_speed)

			print("R Speed: " + str(r_speed) + ", Y Speed: " + str(y_speed))
			#calculate new speeds
			#rotation is not 50 because 50 is too fast
            #MOD: value_speed = int((value_speed)*50)


			#each item in the list represents if the output for each thruster is pos. or neg.
			# ex: in xDirArray, the first element in index 0 (-1) expects that T1 would have a neg. output given a direction
			# WORKING DIRECTIONS
			directionRecieved = ((clientSocket1.recv(1024)).decode())
			#direction data is transferred to socket, then to thrusters, which will tell the thrusters what to do
			directionRecieved = directionRecieved[0]
			#print("direction" + directionRecieved)
			if (directionRecieved == "a"):
				direction = 1
			elif (directionRecieved == "b"):
				direction = -1
				#a is forwards, b is backwards
			else:
				direction = direction
			if debug_l2: print(directionRecieved)
			if debug_l2: print(direction)
			#xDirArray = [-1*direction, 1*direction, -1*direction, 1*direction]
			#yDirArray = [1*direction, 1*direction, -1*direction, -1*direction]
			#rDirArray = [-1, 1, 1, -1]
			xDirArray = [1*direction, 1*direction, 1*direction, -1*direction]
			yDirArray = [-1*direction, 1*direction, 1*direction, 1*direction]
			rDirArray = [1, 1, -1, 1]
			vDirArray = [-1, -1]
			#this section is basically inverse pilot
			#while this code is being processed, directions (left & right, front & back), are inversed when pilot switches cameras

			# array for each horizontal thruster value
			oldThrusterVals = [0, 0, 0, 0]
			# array for each vertical thruster value
			oldVertThrusterVals = [0, 0]

			# loop to collect value for each thruster using horizontal calculation function
			for tNum in range(0,4):
				#goes through code four times
				oldThrusterVals[tNum] = int((calcHorizontal(x_speed, tNum, xDirArray) + calcHorizontal(y_speed, tNum, yDirArray) + calcHorizontal(r_speed, tNum, rDirArray)))
			# loop to collect value for each thruster using vertical calculation function
			for vNum in range(0,2):
				#goes through code two times
				oldVertThrusterVals[vNum] = int((calcVertical(v_speed, vNum, vDirArray)))

			clockArray = [-1, -1, 1, 1]
			clockVertArray = [-1, 1]

			thrusterVals = [0, 0, 0, 0]
			vertThrusterVals = [0, 0]

			for tNum in range(0, 4):
				thrusterVals[tNum] = int(oldThrusterVals[tNum] * clockArray[tNum])

			for vNum in range(0, 2):
				vertThrusterVals[vNum] = int(oldVertThrusterVals[vNum] * clockVertArray[vNum])

		# original print
			# adjusting range
			max_thruster = 0
			for thrusters in range(0,4):
				max_thruster = max(max_thruster, abs(thrusterVals[thrusters]))

			if (max_thruster != 0) and (max_thruster >= 50):
				for thrusters in range(0, 4):
					thrusterVals[thrusters] = int(thrusterVals[thrusters] * (50 / max_thruster))
					#lines 284-291: finds the maximum value of all throttle values, then limits them if needed


			# new lists for the adjusted values for our power functions
			powerThrusterVals = [0, 0, 0, 0]
			powerVertThrusterVals = [0, 0]

			# both for loops adjust the range of the thrusters to 1000-2000
			for thrusters in range(0, 4):
				if (thrusterVals[thrusters] == 0):
					powerThrusterVals[thrusters] = horiz_off_value
				else:
					#powerThrusterVals[thrusters] = 1489 + (((abs(thrusterVals[thrusters]))/thrusterVals[thrusters]) * (25 + (thrusterVals[thrusters] * 4.64)))
					powerThrusterVals[thrusters] = horiz_off_value + ((abs(thrusterVals[thrusters])/thrusterVals[thrusters]) * horiz_thrust_offset) + (thrusterVals[thrusters] * 7.0)
			#was 25 and 4.64
			#using 1489 because 1489 = median of thruster calibration (all thrusters stop at 1489)
			# NOTE - when going full down, the lowest the value goes is 1015 -- fix later --
			for vertThrusters in range(0, 2):
				if debug_l2: print(vertThrusterVals[vertThrusters])
				if (vertThrusterVals[vertThrusters] == 0):
					powerVertThrusterVals[vertThrusters] = vert_off_value
				else:
					#powerVertThrusterVals[vertThrusters] = 1489 + (((abs(vertThrusterVals[vertThrusters]))/vertThrusterVals[vertThrusters]) * (25 + (vertThrusterVals[vertThrusters] * 4.64)))
					powerVertThrusterVals[vertThrusters] = vert_off_value + ((abs(vertThrusterVals[vertThrusters])/vertThrusterVals[vertThrusters]) * vert_thrust_offset) + (vertThrusterVals[vertThrusters] * 7.0)
					#changed from *25 to *50 because verts on this year's robot have a 50 uS deadzone & horizontals only have 25 uS deadzone on each side of center
					#abs(vertThrusterVals[vertThrusters]) just tells direction




			finalHorDiff = abs(powerThrusterVals[1] - horiz_off_value)
			finalVertDiff = abs(powerVertThrusterVals[1] - vert_off_value)
			finalTotal = (finalHorDiff * 4) + (finalVertDiff * 2)
			if (finalTotal != 0):
				percent = (1950/finalTotal)
				#finds percent to display how much we are exceeding power use (ex. exceeding power limit by 5%)
				if (finalTotal > 1950): #max is 2934
					for thruster in range(0, 4):
						Diff = powerThrusterVals[thruster] - horiz_off_value
						newDiff = Diff * (percent)
						powerThrusterVals[thruster] = horiz_off_value + newDiff
					for vertThruster in range(0, 2):
						vertDiff = powerVertThrusterVals[vertThruster] - vert_off_value
						newVertDiff = vertDiff * (percent)
						powerVertThrusterVals[vertThruster] = vert_off_value + newVertDiff
						#finding total thruster throttles and making sure power isnt exceeded
						#main power limiting
						#if power is exceeded, then values are made smaller in line 339

			#print("third print")
			if debug_l2: print(powerThrusterVals)
			#print(powerVertThrusterVals)
			#totalEverything = powerThrusterVals[0] + powerThrusterVals[1] + powerThrusterVals[2] + powerThrusterVals[3] + powerVertThrusterVals[0] + powerVertThrusterVals[1]
			#print(totalEverything)

			throttlePW = int(powerThrusterVals[0]/10000*65536)
			thrusterChannel1.duty_cycle = throttlePW

			throttlePW = int(powerThrusterVals[1]/10000*65536)
			thrusterChannel2.duty_cycle = throttlePW

			throttlePW = int(powerThrusterVals[2]/10000*65536)
			thrusterChannel3.duty_cycle = throttlePW

			throttlePW = int(powerThrusterVals[3]/10000*65536)
			thrusterChannel4.duty_cycle = throttlePW

			throttlePW = int(powerVertThrusterVals[0]/10000*65536)
			thrusterChannel5.duty_cycle = throttlePW

			throttlePW = int(powerVertThrusterVals[1]/10000*65536)
			thrusterChannel6.duty_cycle = throttlePW
			#values(10000*65536) calculates final pw values (that number can be processed by esc)
			#sending it to specific thrusters
			#power calculations
	#    	time.sleep(1)

		except ValueError:
			print("Error")
			check = (clientSocket.recv(1024)).decode()
			print("check: " + check)

if __name__ == "__main__":
    main()
