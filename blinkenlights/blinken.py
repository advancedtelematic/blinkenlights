import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

ledPin = 12

GPIO.setup(ledPin, GPIO.OUT)

def dit():
	print("LED turning on.")
	GPIO.output(ledPin, GPIO.HIGH)
	time.sleep(0.5)
	print("LED turning off.")
	GPIO.output(ledPin, GPIO.LOW) 
	time.sleep(0.5)

def dat():
	print("LED turning on.")
	GPIO.output(ledPin, GPIO.HIGH)
	time.sleep(1.5)
	print("LED turning off.")
	GPIO.output(ledPin, GPIO.LOW) 
	time.sleep(0.5)

def char_space():
	time.sleep(1)

def word_space():
	time.sleep(7)

def sos():
	dit()
	dit()
	dit()
	char_space()
	dat()
	dat()
	dat()
	char_space()
	dit()
	dit()
	dit()
	word_space()

while True:
	sos()
