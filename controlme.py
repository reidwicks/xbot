#!usr/bin/bash
import fileinput

for line in fileinput.input():
    print(line)
