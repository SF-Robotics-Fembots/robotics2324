import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

num = 2

while num == 2:
	pin = int(input("enter pin - front (21) or back (20): "))
	value = int(input("enter high (1) or low (0) or 2 to exit: "))
	if value == 2:
		num = 2
	else:
		GPIO.output(pin, value)
