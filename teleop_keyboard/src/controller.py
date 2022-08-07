#!/usr/bin/python3
import keyboard
import socket
import time
import rospy

rospy.init_node('controller_keyboard')
s = socket.socket()
s.connect(('192.168.30.17',9230))
while True:
	if(keyboard.is_pressed('w')):
		print('forward')
		s.send(bytes('w', "utf-8"))
	elif(keyboard.is_pressed('a')):
		print('hard-left')
		s.send(bytes('a', "utf-8"))
	elif(keyboard.is_pressed('d')):
		print('hard-right')
		s.send(bytes('d', "utf-8"))
	else:
		print('stop')
		s.send(bytes('s', "utf-8"))
	time.sleep(0.2)
