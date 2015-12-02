import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.



# game loop
while 1:
    heights = []

    space_x, space_y = [int(i) for i in input().split()]

    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
        heights.append(mountain_h)

    tallest_mountain = heights.index(max(heights))

    if(space_x == tallest_mountain):
        print("FIRE")
    else:
        print("HOLD")
