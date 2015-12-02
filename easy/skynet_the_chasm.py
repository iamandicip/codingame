import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

road = int(input())  # the length of the road before the gap.
gap = int(input())  # the length of the gap.
platform = int(input())  # the length of the landing platform.

# game loop
while 1:
    speed = int(input())  # the motorbike's speed.
    coord_x = int(input())  # the position on the road of the motorbike.

    action = ""

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    if(road + gap > coord_x + speed):
        if(speed < gap + 1):
            action = "SPEED"
        elif(speed > gap + 1):
            action = "SLOW"
        else:
            action = "WAIT"
    elif(road + gap <= coord_x + speed and coord_x < road + gap):
        action = "JUMP"
    elif(coord_x >= road + gap):
        action = "SLOW"

    # A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.
    print(action)
