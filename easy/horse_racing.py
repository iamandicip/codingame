import sys
import math

strengths = []
dif = 10000000

n = int(input())
for i in range(n):
    pi = int(input())
    strengths.append(pi)

strengths.sort()

for i in range(len(strengths) - 1):
    d = abs(strengths[i] - strengths[i+1])
    if(d < dif):
        dif = d

print(dif)
