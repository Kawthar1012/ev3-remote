"""
robot.py

the robot class that sorts the objects depending on their colors. 

"""
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


class Robot(object):
    def __init__(self, camera=None):
        self.POSSIBLE_COLORS = ['RED', 'GREEN', 'BLUE']
        
        # Initialize the EV3 brick.
        self.ev3 = EV3Brick()

        # Initialize the motors that drive the conveyor belt and eject the objects.
        self.belt_motor = Motor(Port.D)
        self.feed_motor = Motor(Port.A)

        # Initialize the Touch Sensor. It is used to detect when the belt motor has
        # moved the sorter module all the way to the left.
        self.touch_sensor = TouchSensor(Port.S2)

    def debug(self, debug):
        self.ev3.speaker.say(debug)

    def init(self):
        # Get the feed motor in the correct starting position.
        # This is done by running the motor forward until it stalls. This
        # means that it cannot move any further. From this end point, the motor
        # rotates backward by 180 degrees. Then it is in the starting position.
        self.feed_motor.run_until_stalled(120, duty_limit=50)
        self.feed_motor.run_angle(450, -200)

        # Get the conveyor belt motor in the correct starting position.
        # This is done by first running the belt motor backward until the
        # touch sensor becomes pressed. Then the motor stops, and the the angle is
        # reset to zero. This means that when it rotates backward to zero later
        # on, it returns to this starting position.
        self.belt_motor.run(-500)
        while not self.touch_sensor.pressed():
            pass
        self.belt_motor.stop()
        wait(1000)
        self.belt_motor.reset_angle(0)

        self.ev3.speaker.say('ready')

    def react(self,msg):
        if (msg == 'left'):
            self.ev3.speaker.say("left")
            self.belt_motor.run_target(500, 0)
        elif (msg == 'right'):
            self.ev3.speaker.say("right")
            self.belt_motor.run_target(500, 550)
        elif (msg == 'start'):
            self.ev3.speaker.say("start")
            self.sort("BLUE")

    def sort(self, color):
        # Play a sound and show an image to indicate that we are done scanning.
        self.ev3.speaker.play_file(SoundFile.READY)
        self.ev3.screen.load_image(ImageFile.EV3)
        # for color in color_list:
            # Wait for one second between each sorting action.
        wait(1000)

        # Run the conveyor belt motor to the right position based on the color.
        if color == 'BLUE':
            self.ev3.speaker.say('blue')
            self.belt_motor.run_target(500, 10)
        elif color == 'GREEN':
            self.ev3.speaker.say('green')
            self.belt_motor.run_target(500, 132)
        elif color == 'YELLOW':
            self.ev3.speaker.say('yellow')
            self.belt_motor.run_target(500, 360)
        elif color == 'RED':
            self.ev3.speaker.say('red')
            self.belt_motor.run_target(500, 530)
        else:
            self.ev3.speaker.say('not recognized')
            self.belt_motor.run_target(500, 10)

        # Now that the conveyor belt is in the correct position, eject the
        # colored object.
        self.feed_motor.run_angle(1500, 180)
        self.feed_motor.run_angle(1500, -180)


