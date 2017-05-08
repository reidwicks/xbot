#!usr/bin/bash
import fileinput

for line in fileinput.input():
    for item in line.split():
        if item == "du:1":
            print("Up")
        elif item == "dd:1":
            print("Down")
        elif item == "dl:1":
            print("Left")
        elif item == "dr:1":
            print("Right")
