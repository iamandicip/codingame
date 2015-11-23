import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

lowest_positive = 5526
highest_negative = -273

temperature = 0

if(temps):

    have_negatives = False
    have_positives = False
    
    tmps = list(map(int, temps.split(' ')))
    
    if(max(tmps) > 0):
        have_positives = True
        
    if(min(tmps) < 0):
        have_negatives = True
    
    for t in tmps:
        if(t < 0 and t >= highest_negative):
            highest_negative = t
        
        if(t > 0 and t <= lowest_positive):
            lowest_positive = t
    
    if(not have_positives):
        temperature = highest_negative
        
    elif(not have_negatives):
        temperature = lowest_positive
    
    elif(lowest_positive <= abs(highest_negative)):
        temperature = lowest_positive
    
    else:
        temperature = highest_negative

print(temperature)