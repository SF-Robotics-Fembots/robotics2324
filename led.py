import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
GPIO.setup(13,GPIO.OUT)
print ("LED on")
GPIO.output(13,GPIO.HIGH)
time.sleep(3)
print ("LED off")
GPIO.output(13,GPIO.LOW)

    
