<<<<<<< HEAD
import sys
import math

# CodinGame planet is being attacked by slimy insectoid aliens.
# <---
# Hint:To protect the planet, you can implement the pseudo-code provided in the statement, below the player.


# game loop
while 1:
    enemy_1 = input()  # name of enemy 1
    dist_1 = int(input())  # distance to enemy 1
    enemy_2 = input()  # name of enemy 2
    dist_2 = int(input())  # distance to enemy 2

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # You have to output a correct ship name to shoot ("Buzz", enemy1, enemy2, ...)
    if dist_1 > dist_2:
        print(enemy_2)
    else:
=======
import sys
import math

# CodinGame planet is being attacked by slimy insectoid aliens.
# <---
# Hint:To protect the planet, you can implement the pseudo-code provided in the statement, below the player.


# game loop
while 1:
    enemy_1 = input()  # name of enemy 1
    dist_1 = int(input())  # distance to enemy 1
    enemy_2 = input()  # name of enemy 2
    dist_2 = int(input())  # distance to enemy 2

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # You have to output a correct ship name to shoot ("Buzz", enemy1, enemy2, ...)
    if dist_1 > dist_2:
        print(enemy_2)
    else:
>>>>>>> 05b9259cb866797e808333093e85a493ada75d07
        print(enemy_1)