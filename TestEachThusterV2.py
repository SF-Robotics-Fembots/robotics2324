import lgpio
#works w/ sockets
import board	#pip install board
import busio	#pip install adafruit-blinka
import adafruit_pca9685 #pip install adafruit-circuitpython-pca9685
from adafruit_servokit import ServoKit #pip install adafruit-circuitpython-servokit
import time
import socket

def main():

	i2c = busio.I2C(board.SCL, board.SDA)
	shield = adafruit_pca9685.PCA9685(i2c)
	kit = ServoKit(channels=16)
	shield.frequency = 96
	#changed the shield frequency (pwm) to 96 Hz
	#100 in Hz, meaning shield runs at 100 times a second
	#100 Hz = cycle time for PWM signal
	#meaning robot speed can change 100 times a second
	
	channelNums = [0, 15, 2, 13, 1, 14]
	thrusterArray = []
	FwdPWM = int(1800/10000*65536)
	BackPWM = int(1200/10000*65536)
	stopPWM = int(1480/10000*65536)
	print("channelNums", channelNums)

	#Setup and Initialize
	for i in range (6):
		go = input("Press any key to initialize thruster " + str(i+1))
		#print("i ", i)
		#print("channelNums[i]", channelNums[i])
		#a = channelNums[i]
		thrusterArray.append(shield.channels[channelNums[i]])
		#bob = shield.channels[a]
		#  initialize thrusters - set to full foward then to stop
		thrusterArray[i].duty_cycle = FwdPWM #set to full forward
		time.sleep(0.25)
		thrusterArray[i].duty_cycle = stopPWM
		time.sleep(0.25)

	#Run Full Foward for 0.5s, full reverse for 0.5s, stop
	for i in range (6):
		go = input("Press any key to run thruster " + str(i+1))
		thrusterArray[i].duty_cycle = FwdPWM #set to forward
		time.sleep(0.5)
		thrusterArray[i].duty_cycle = stopPWM #stop
		time.sleep(0.5)
		thrusterArray[i].duty_cycle = BackPWM #set to backward
		time.sleep(0.5)
		thrusterArray[i].duty_cycle = stopPWM #stop
		time.sleep(0.25)


if __name__ == "__main__":
    main()
