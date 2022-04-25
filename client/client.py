#!/usr/bin/env pybricks-micropython
"""
client.py 

the client class to be run on the brick
"""
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.hubs import EV3Brick

import socket

from robot import Robot

class Client(object):
    def __init__(self, addr,  port=12345):
        self.socket =  socket.socket()
        self.port = port
        self.addr = addr

        self.socket.connect((self.addr, self.port))
        #  self.ev3.speaker.say('connected to server')
        self.robot = Robot()
        
    def start(self):
        #self.robot.debug(self.socket.recv(1024).decode())
        self.robot.init()
        while True:
            msg = self.socket.recv(1024).decode()
            self.robot.react(msg)
        
        self.socket.close()

if __name__ == '__main__':
    # change for the ip of your computer
    client = Client('212.25.146.185', 12345)
    client.start()