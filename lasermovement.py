#!/usr/bin/python
# necessary imports from Adafruit HAT Library
From Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import time
import atexit
import threading
import random

#create a default object, no changes to I2C address or frequency
laserhat = Adafruit_MotorHAT(addr = 0x61) #creates a top level motor hat object

#create empty threads (these will hold the stepper 3 and 4 threads)
st3 = threading.Thread()
st4 = threading.Thread()

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    laserhat.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    laserhat.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    laserhat.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    laserhat.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

#determining number of steps per minute
myStepper3 = mh.getStepper(200, 3)      # 200 steps/rev, motor port #3
myStepper4 = mh.getStepper(200, 4)      # 200 steps/rev, motor port #4
myStepper3.setSpeed(30)          # 30 RPM
myStepper4.setSpeed(30)          # 30 RPM

