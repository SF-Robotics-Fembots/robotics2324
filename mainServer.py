import pygame
import time
import socket
import threading
import joystickServer
import grippertopside
#import lightServer
#import hatTest
#import saltWater
import pilotInverseServer
#import lazersServer
#import fryServer

global ip_server
ip_server = "192.168.1.100"

joystickCode = threading.Thread(target=joystickServer.main, args = (ip_server,))
#lightCode = threading.Thread(target=lightServer.main, args = ())
#hatCode = threading.Thread(target=hatTest.main, args = (ip_server,))
#saltWaterCode = threading.Thread(target=saltWater.main, args = ())
inverseCode = threading.Thread(target=pilotInverseServer.main, args = (ip_server,))
grippertopsideCode = threading.Thread(target=grippertopside.main, args = (ip_server,))
#lazersCode = threading.Thread(target=lazersServer.main, args = ())
#fryCode = threading.Thread(target=fryServer.main, args = ())


joystickCode.start()
grippertopsideCode.start()
#lightCode.start()
#hatCode.start()
#saltWaterCode.start()
inverseCode.start()
#lazersCode.start()
#fryCode.start()

joystickCode.join()
inverseCode.join()
grippertopsideCode.start()