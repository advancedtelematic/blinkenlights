import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

ledPin = 12

GPIO.setup(ledPin, GPIO.OUT)

def dit():
	print("LED turning on.")
	GPIO.output(ledPin, GPIO.HIGH)
	time.sleep(0.2)
	print("LED turning off.")
	GPIO.output(ledPin, GPIO.LOW) 
	time.sleep(0.2)

def dat():
	print("LED turning on.")
	GPIO.output(ledPin, GPIO.HIGH)
	time.sleep(0.5)
	print("LED turning off.")
	GPIO.output(ledPin, GPIO.LOW) 
	time.sleep(0.2)

def char_space():
	time.sleep(0.2)

def word_space():
	time.sleep(1)

def ota_connect():
	dat()
	dat()
	dat()
	char_space()

	dat()
	char_space()

	dit()
	dat()
	char_space()

	dat()
	dit()
	dat()
	dit()
	char_space()

	dat()
	dat()
	dat()
	char_space()


	dit()
	dat()
	char_space()

	dit()
	dat()
	char_space()

	dit()
	char_space()

	dat()
	dit()
	dat()
	dit()
	char_space()

	dat()
	char_space()

while True:
	ota_connect()
