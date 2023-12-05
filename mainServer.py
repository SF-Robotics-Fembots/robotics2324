import pygame
import time
import socket
import threading
import joystickServer
#import lightServer
import hatTest
#import saltWater
import pilotInverseServer
#import lazersServer
#import fryServer


joystickCode = threading.Thread(target=joystickServer.main, args = ())
#lightCode = threading.Thread(target=lightServer.main, args = ())
hatCode = threading.Thread(target=hatTest.main, args = ())
#saltWaterCode = threading.Thread(target=saltWater.main, args = ())
inverseCode = threading.Thread(target=pilotInverseServer.main, args = ())
#lazersCode = threading.Thread(target=lazersServer.main, args = ())
#fryCode = threading.Thread(target=fryServer.main, args = ())


joystickCode.start()
#lightCode.start()
hatCode.start()
#saltWaterCode.start()
inverseCode.start()
#lazersCode.start()
#fryCode.start()