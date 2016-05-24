#!/usr/bin/python

# Import required libraries
import sys
import RPi.GPIO as GPIO # GPIO library we need to use the GPIO pins
import time # time library for sleep function

# GPIO pins for pump
StepPinForward=32
StepPinBackward=36
GPIO.setmode(GPIO.BOARD)
GPIO.setup(StepPinForward, GPIO.OUT)
GPIO.setup(StepPinBackward, GPIO.OUT)

# GPIO pins for water sensor
channel = 29 #5
# Set the GPIO pin to an input
GPIO.setup(channel, GPIO.IN)

def soilsensor(channel):  
    if GPIO.input(channel):
        print "Turning Water Pump On!"
        pumpforward(5)
        #GPIO.output(StepPinForward, GPIO.LOW)
        #GPIO.cleanup()

    else:       
        print "Enough Water. Now Stopping Water Pump"
        GPIO.output(StepPinForward, GPIO.LOW)

# Function for turning water pump on to suck from tub & push to plants
def pumpforward(x):
    GPIO.output(StepPinForward, GPIO.HIGH)
    print "forwarding running pump"
    time.sleep(10)
    GPIO.output(StepPinForward, GPIO.LOW)

# Function for reversing pump in order to put excess water in tubes back into tub
def pumpbackward(x):
    GPIO.output(StepPinBackward, GPIO.HIGH)
    print "backward running pump"
    time.sleep(10)
    GPIO.output(StepPinBackward, GPIO.LOW)    
    
# Tells script to watch gpio pin and let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)

# Assigns a function to the GPIO pin so when a change on the pin from above add_event_detect, run this function
GPIO.add_event_callback(channel, soilsensor)

# Infinte loop to keep our script running
while True:
	# Tells our script to wait 0.1 of a second so the script doesnt hog all of the CPU
	time.sleep(0.1)
