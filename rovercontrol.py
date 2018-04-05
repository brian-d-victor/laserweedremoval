#!/usr/bin/python
# necessary imports from Adafruit Hat library 
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import time
import atexit
import threading
import random

# create a default object, no changes to I2C address or frequency
#rover hat is default address 0x60
roverhat = Adafruit_MotorHAT(addr = 0x60)   # declares the hat object for the two rover motors

# create empty threads (these will hold the stepper 1 and 2 threads)
st1 = threading.Thread()
st2 = threading.Thread()

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    roverhat.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    roverhat.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    roverhat.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    roverhat.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

#Code to determine number steps/rev and number RPM 

myStepper1 = roverhat.getStepper(200, 1)      # 200 steps/rev, motor port #1
myStepper2 = roverhat.getStepper(200, 2)      # 200 steps/rev, motor port #2
myStepper1.setSpeed(30)          # 30 RPM
myStepper2.setSpeed(30)          # 30 RPM

#
stepstyles = [Adafruit_MotorHAT.SINGLE, Adafruit_MotorHAT.DOUBLE, Adafruit_MotorHAT.INTERLEAVE, Adafruit_MotorHAT.MICROSTEP] 





