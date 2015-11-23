import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

alphabet = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ?")
replacement_char="?"

idx_replacement = alphabet.index(replacement_char)

l = int(input())
h = int(input())
t = input()

for i in range(h):
    row = input()
    
    text = list(t)

    for letter in text:
        try:
            l_idx = alphabet.index(letter.upper())
        except ValueError:
            l_idx = idx_replacement
        
        idx = l_idx * l
        
        print(row[idx : idx + l], end="")