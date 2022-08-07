#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Ena,In1,In2 = 2,3,4
GPIO.setup(Ena,GPIO.OUT)
GPIO.setup(In1,GPIO.OUT)
GPIO.setup(In2,GPIO.OUT)
pwm = GPIO.PWM(Ena,100)
pwm.start(0)
PWM_VAL = 10

msg = """
Motor Code for AAIBOT 2022 :
Press the required key and press enter to execute commad!
---------------------------
Moving around:
        w    
   a    s    d
   
"""
def forward():
        GPIO.output(In2,GPIO.HIGH)
        print("In2 : 1")
        GPIO.output(In1,GPIO.HIGH)
        print("In1 : 1")
        print("Forward")

def hard_left():
        GPIO.output(In2,GPIO.HIGH)
        print("In2 : 1")
        GPIO.output(In1,GPIO.LOW)
        print("In1 : 0")
        print("hard-left")


def hard_right():
        GPIO.output(In2,GPIO.LOW)
        print("In2 : 0")
        GPIO.output(In1,GPIO.HIGH)
        print("In1 : 1")
        print("hard-right")

def stop():
        GPIO.output(In1,GPIO.LOW)
        GPIO.output(In2,GPIO.LOW)
        print("In1 : 0")
        print("In2 : 0")
        print("Stop")

print(msg)
while True:
        #print('Loop Running')
        # Insert the function to set direction
        choice = input("Enter Command :  ")
        if(choice =='w'):
                forward()
        elif(choice=='a'):
                hard_left()
        elif(choice=='d'):
                hard_right()
        else:
                stop()
        pwm.ChangeDutyCycle(10)
        print(f"PWM :{PWM_VAL} ")

