import sys
import math

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

grid = []

for i in range(height):
    line = input()  # width characters, each either 0 or .
    grid.append(list(line))

#print(grid, file=sys.stderr)

for j in range(height):
    for i in range(width):
        current_cell = grid[j][i]

        if(current_cell == "0"):
            current_node = str(i) + " " + str(j)
            right_neighbour_node = "-1 -1"
            bottom_neighbour_node = "-1 -1"

            k = i
            right_neighbour_found = False
            while(k < width - 1 and not right_neighbour_found):
                k += 1
                right_neighbour_cell = grid[j][k]
                if(right_neighbour_cell == "0"):
                    right_neighbour_node = str(k) + " " + str(j)
                    right_neighbour_found = True

            l = j
            bottom_neighbour_found = False
            while(l < height - 1 and not bottom_neighbour_found):
                l+=1
                bottom_neigbour_cell = grid[l][i]
                if(bottom_neigbour_cell == "0"):
                    bottom_neighbour_node = str(i) + " " + str(l)
                    bottom_neighbour_found = True

            print(current_node + " " + right_neighbour_node + " " + bottom_neighbour_node)
