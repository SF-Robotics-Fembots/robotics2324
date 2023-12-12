import lgpio
import pygame
import board
import busio
import adafruit_pca9685
from adafruit_servokit import ServoKit
import time
import threading
import socket
import gripperbottomside
#import servo
import thrusters2324
#import thrustersmod
#import saltWater
#import lazers
#import lightSource
#import fry

# library setup
pygame.init()
i2c = busio.I2C(board.SCL, board.SDA)
shield = adafruit_pca9685.PCA9685(i2c)
kit = ServoKit(channels=16)
shield.frequency = 100

#global ip variable setup
global ip_server
ip_server = "192.168.1.107"
    
thrusterChannel1 = shield.channels[0]
thrusterChannel2 = shield.channels[1]
thrusterChannel3 = shield.channels[2]
thrusterChannel4 = shield.channels[3]
thrusterChannel5 = shield.channels[4]
thrusterChannel6 = shield.channels[5]
thrusterChannel1.duty_cycle = 0x2666
    
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

thrusterCode = threading.Thread(target=thrusters2324.main, args = (ip_server,))
gripperbottomsideCode = threading.Thread(target = gripperbottomside.main, args = (ip_server,))
#servoCode = threading.Thread(target=servo.main, args = (ip_server,))
#saltWaterCode = threading.Thread(target=saltWater.main, args = (ip_server,))
#lazersCode = threading.Thread(target=lazers.main, args= (ip_server,))
#lightSourceCode= threading.Thread(target=lightSource.main, args = (ip_server,))
#fryCode = threading.Thread(target= fry.main, args = (ip_server,))

#servoCode.start()
thrusterCode.start()
#saltWaterCode.start() 
#lazersCode.start()
#lightSourceCode.start()
#fryCode.start()
