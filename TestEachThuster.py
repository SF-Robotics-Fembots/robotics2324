import lgpio
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

def main():
	# library setup
	pygame.init()

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

	thrusterChannel1 = shield.channels[0]
	thrusterChannel2 = shield.channels[15]
	thrusterChannel3 = shield.channels[2]
	thrusterChannel4 = shield.channels[13] #changed from 3, 4, 5
	thrusterChannel5 = shield.channels[1]
	thrusterChannel6 = shield.channels[14]
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


	throttlePW = int(2000/10000*65536)
	thrusterChannel1.duty_cycle = throttlePW

	throttlePW = int(2000/10000*65536)
	thrusterChannel2.duty_cycle = throttlePW

	throttlePW = int(2000/10000*65536)
	thrusterChannel3.duty_cycle = throttlePW

	throttlePW = int(2000/10000*65536)
	thrusterChannel4.duty_cycle = throttlePW

	throttlePW = int(2000/10000*65536)
	thrusterChannel5.duty_cycle = throttlePW

	throttlePW = int(2000/10000*65536)
	thrusterChannel6.duty_cycle = throttlePW

	time.sleep(2)

	throttlePW = int(1480/10000*65536)
	thrusterChannel1.duty_cycle = throttlePW

	throttlePW = int(1480/10000*65536)
	thrusterChannel2.duty_cycle = throttlePW

	throttlePW = int(1480/10000*65536)
	thrusterChannel3.duty_cycle = throttlePW

	throttlePW = int(1480/10000*65536)
	thrusterChannel4.duty_cycle = throttlePW

	throttlePW = int(1480/10000*65536)
	thrusterChannel5.duty_cycle = 2000

	throttlePW = int(1480/10000*65536)
	thrusterChannel6.duty_cycle = throttlePW
	
	time.sleep(1)


if __name__ == "__main__":
    main()
