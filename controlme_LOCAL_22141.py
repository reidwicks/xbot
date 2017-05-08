#!usr/bin/python

import fileinput

buttons = {"du:1" : "Up",
           "dd:1" : "Down",
           "dl:1" : "Left",
           "dr:1" : "Right",
           "back:1" : "Back",
           "guide:1" : "Guide",
           "start:1" : "Start",
           "TL:1" : "Left joystick button",
           "TR:1" : "Right joystick button",
           "A:1" : "A",
           "B:1" : "B",
           "X:1" : "X",
           "Y:1" : "Y",
           "LB:1" : "Left bumper",
           "RB:1" : "Right bumper",
           "LT:255" : "Left trigger (fully depressed)",
           "RT:255" : "Right trigger (fully depressed)",
           }

for line in fileinput.input():
    for item in line.split():
        if item in buttons:
            print(buttons[item])
