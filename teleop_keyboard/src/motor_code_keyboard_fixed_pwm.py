#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import socket
import rospy

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Ena, In1, In2 = 12, 2, 3
Enb, In3, In4 = 13, 0, 1
GPIO.setup(Ena, GPIO.OUT)
GPIO.setup(In1, GPIO.OUT)
GPIO.setup(In2, GPIO.OUT)

GPIO.setup(Enb, GPIO.OUT)
GPIO.setup(In3, GPIO.OUT)
GPIO.setup(In4, GPIO.OUT)


pwml = GPIO.PWM(Ena, 100)
pwml.start(0)

pwmr = GPIO.PWM(Enb, 100)
pwmr.start(0)


PWM_VAL = 30

msg = """
Motor Code for AAIBOT 2022 :
Press the required key and press enter to execute commad!
---------------------------
Moving around:

        w  
          
   a    s    d
   
w : Full Forward
a : Hard Left
d : Hard Right
s : Stop
q : to quit application   
"""

rospy.init_node('motor_code_keyboard_fixed_pwm')

def forward():
    GPIO.output(In2, GPIO.LOW)
    print("In2 : 0")
    GPIO.output(In1, GPIO.HIGH)
    print("In1 : 1")
    GPIO.output(In4, GPIO.HIGH)
    print("In4 : 1")
    GPIO.output(In3, GPIO.LOW)
    print("In3 : 0")
    print("Forward")


def hard_right():
    GPIO.output(In2, GPIO.HIGH)
    print("In2 : 1")
    GPIO.output(In1, GPIO.LOW)
    print("In1 : 0")
    GPIO.output(In4, GPIO.HIGH)
    print("In4 : 1")
    GPIO.output(In3, GPIO.LOW)
    print("In3 : 0")
    print("hard-right")

def hard_left():
    GPIO.output(In2, GPIO.LOW)
    print("In2 : 0")
    GPIO.output(In1, GPIO.HIGH)
    print("In1 : 1")
    GPIO.output(In4, GPIO.LOW)
    print("In4 : 1")
    GPIO.output(In3, GPIO.HIGH)
    print("In3 : 0")
    print("hard-left")

def stop():
    GPIO.output(In1, GPIO.LOW)
    GPIO.output(In2, GPIO.LOW)
    GPIO.output(In4, GPIO.LOW)
    GPIO.output(In3, GPIO.LOW)
    print("In1 : 0")
    print("In2 : 0")
    print("In3 : 0")
    print("In4 : 0")
    print("Stop")

print("Waiting for controller to connect")
s = socket.socket()
s.bind(('192.168.30.17', 9230))
s.listen(0)
#print("Controller Connected")
#print(msg)
while True:
    #print('Loop Running')
    # Insert the function to set direction
    """
    choice = input("Enter Command :  ")
    if(choice == 'w'):
        forward()
    elif(choice == 'a'):
        hard_left()
    elif(choice == 'd'):
        hard_right()
    elif(choice == 'q'):
        break
    else:
        stop()
    """
    client,addr = s.accept()
    print("Connected to Controller!")
    print(msg)
    while True:
        data = client.recv(32).decode("utf-8")
        #print(data)
        if(len(data))==0:
            break
        elif(data=='w'):
            forward()
        elif(data=='a'):
            hard_left()
        elif(data=='d'):
            hard_right()
        else:
            stop()
        pwml.ChangeDutyCycle(PWM_VAL)
        pwmr.ChangeDutyCycle(PWM_VAL)
    client.close()
    #print(f"PWM :{PWM_VAL} ")
