# import RPi.GPIO as GPIO
import time
import subprocess

# GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False)

ledPin = 12

# GPIO.setup(ledPin, GPIO.OUT)

unit = 0.2
ditTime = unit
dahTime = unit * 3
intra_characterTime = unit
inter_characterTime = unit * 3
spaceTime = unit * 7

def dit():
        print("Dit: LED turning on.")
	#GPIO.output(ledPin, GPIO.HIGH)
	time.sleep(ditTime)
        print("Dit: LED turning off.")
	#GPIO.output(ledPin, GPIO.LOW)

def dah():
        print("Dah: LED turning on.")
	#GPIO.output(ledPin, GPIO.HIGH)
	time.sleep(dahTime)
        print("Dah: LED turning off.")
	#GPIO.output(ledPin, GPIO.LOW)

def intra_character_space():
        print("intra_character")
	time.sleep(intra_characterTime)

def inter_character_space():
        print("intER_character")
	time.sleep(inter_characterTime)

def inter_word_space():
	time.sleep(spaceTime)

letters = {
        'A': [dit, dah],
        'B': [dah, dit, dit, dit],
        'C': [dah, dit, dah, dit],
        'D': [dah, dit, dit],
        'E': [dit],
        'F': [dit, dit, dah, dit],
        'G': [dah, dah, dit],
        'H': [dit, dit, dit, dit],
        'I': [dit, dit],
        'J': [dit, dah, dah, dah],
        'K': [dah, dit, dah],
        'L': [dit, dah, dah, dah],
        'M': [dah, dah],
        'N': [dah, dit],
        'O': [dah, dah, dah],
        'P': [dit, dah, dah, dit],
        'Q': [dah, dah, dit, dah],
        'R': [dit, dah, dit],
        'S': [dit, dit, dit],
        'T': [dah],
        'U': [dit, dit, dah],
        'V': [dit, dit, dit, dah],
        'W': [dit, dah, dah],
        'X': [dah, dit, dit, dah],
        'Y': [dah, dit, dah, dah],
        'Z': [dah, dah, dit, dit],
        ' ': [inter_word_space]
        }

def joinit(iterable, delimiter):
    it = iter(iterable)
    yield next(it)
    for x in it:
        yield delimiter
        yield x

def letterToMorse(string):
    chars = list(string.upper())
    for char in chars:
        print("char: " + char)
        inter_character_space()
        if char in letters:
            withIntraChar = joinit(letters[char], intra_character_space)
            for d in withIntraChar:
                d()
        else:
            print("char: .")
            inter_word_space()


f = subprocess.Popen(['journalctl','-fu','unbound'],\
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
while True:
    line = f.stdout.readline()
    letterToMorse(line)
