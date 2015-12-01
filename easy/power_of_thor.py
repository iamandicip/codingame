import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

thor_x = initial_tx
thor_y = initial_ty

direction_x = ""
direction_y = ""

MAX_Y = 17
MAX_X = 39

# game loop
while 1:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    if(light_y > thor_y and thor_y < MAX_Y):
        direction_y = "S"
        thor_y += 1
    elif (light_y < thor_y and thor_y > 0):
        direction_y = "N"
        thor_y -= 1
    else:
        direction_y = ""

    if(light_x > thor_x and thor_x < MAX_X):
        direction_x = "E"
        thor_x += 1
    elif(light_x < thor_x and thor_x > 0):
        direction_x = "W"
        thor_x -= 1
    else:
        direction_x = ""

    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(direction_y + direction_x)
