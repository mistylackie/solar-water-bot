#!/usr/bin/python
# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

def MotorDirection(direction):
    # Physical pins 11,15,16,18
    # GPIO Pins GPIO17,GPIO22,GPIO23,GPIO24
    # Code the StepPins to GPIO pins
    StepPins = [17,22,23,24]


    # Set all pins as output
    for pin in StepPins:
        #print "Setup pins"
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin, False)
         
    # Define advanced sequence
    # as shown in manufacturers datasheet
    Seq = [[1,0,0,1],
           [1,0,0,0],
           [1,1,0,0],
           [0,1,0,0],
           [0,1,1,0],
           [0,0,1,0],
           [0,0,1,1],
           [0,0,0,1]]

    StepCount = len(Seq)

    # Set to 1 or 2 for clockwise
    # Set to -1 or -2 for anti-clockwise
    StepDirection = direction
     
    # Read wait time from command line
    if len(sys.argv)>1:
        WaitTime = int(sys.argv[1])/float(1000)
    else:
        WaitTime = 4/float(1000)
     
    # Initialise variables
    StepCounter = 0
    StepDuration = 25000
    CountDuration = 0
     
    # Start main loop
    while True:
     
        for pin in range(0,4):
            xpin=StepPins[pin]# Get GPIO
            if Seq[StepCounter][pin]!=0:
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)
     
        StepCounter += StepDirection
     
        # If we reach the end of the sequence start again
        if (StepCounter>=StepCount):
            StepCounter = 0
        if (StepCounter<0):
            StepCounter = StepCount+StepDirection
         
        CountDuration = CountDuration + 1

        if (CountDuration==StepDuration):
            print "Steps Done!"
            break

        # Wait before moving on
        time.sleep(WaitTime)
        

      
