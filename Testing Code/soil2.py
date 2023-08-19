#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# GPIO SETUP
channel1 = 20
channel2 = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel1, GPIO.IN)
GPIO.setup(channel2, GPIO.IN)


def callback(channel1,channel2):
    if GPIO.input(channel1,channel2):
        print
        "Water Detected!"
    else:
        print
        "Water Detected!"


GPIO.add_event_detect(channel1, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(channel2, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel1, callback)  # assign function to GPIO PIN, Run function on change
GPIO.add_event_callback(channel2, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
    time.sleep(1)