# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
#GPIO.setmode(GPIO.BCM)
mode=GPIO.getmode()
print " mode ="+str(mode)
GPIO.cleanup()

# Define GPIO signals to use

StepPinForward=32
StepPinBackward=36

GPIO.setmode(GPIO.BOARD)
GPIO.setup(StepPinForward, GPIO.OUT)
GPIO.setup(StepPinBackward, GPIO.OUT)

def forward(x):
    GPIO.output(StepPinBackward, GPIO.HIGH)
    print "backward running pump"
    time.sleep(10)
    GPIO.output(StepPinBackward, GPIO.LOW)


print "backward pump"
forward(5)

print "Stopping motor"
GPIO.cleanup()
