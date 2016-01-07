import sys
import math
import random

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

target = ()

MAX_X = 34
MAX_Y = 19

def next_cell_busy(current_position, target, map):
    if(current_position == target):
        return False

    next_cell = "."
    x1 = current_position[1]
    y1 = current_position[0]
    x2 = target[1]
    y2 = target[0]
    if(x1 == x2):
        if(y1 < y2): #going down
            next_cell = map[y1 + 1][x1]
        else: #going up
            next_cell = map[y1 - 1][x1]
    elif(x1 < x2): #going right
        next_cell = map[y1][x1 + 1]
    else: #going left
        next_cell = map[y1][x1 - 1]

    return next_cell != "."

def find_empty_cell(current_position, target, map):
    empty_cell = target
    x1 = current_position[1]
    y1 = current_position[0]
    x2 = target[1]
    y2 = target[0]
    if(x1 == x2):
        if(y1 < y2): #going down
            if(x1 > 1 and map[y1][x1 - 1] == "."):
                empty_cell = (y1, x1 - 1)
            elif(x1 < MAX_X - 1 and map[y1][x1 + 1] == "."):
                empty_cell = (y1, x1 + 1)
        else: #going up
            if(x < MAX_X - 1 and map[y1][x1 + 1] == "."):
                empty_cell = (y1, x1 + 1)
            elif(x > 1 and map[y1][x1 - 1] == "."):
                empty_cell = (y1, x1 - 1)
    elif(x1 < x2): #going right
        if(y1 <= y2 and map[y1 + 1][x1] == "." ):
            empty_cell = (y1 + 1, x1)
        elif(y1 > y2 and map[y1 - 1][x1] == "."):
            empty_cell = (y1 - 1, x1)
    else: #going left
        if(y1 > y2):
            if(map[y1 - 1][x1] == "."):
                empty_cell = (y1 - 1, x1)
            elif(y1 < MAX_Y - 1 and map[y1 + 1][x1] == "."):
                empty_cell = (y1 + 1, x1)
        elif(y1 <= y2):
            if(map[y1 + 1][x1] == "."):
                empty_cell = (y1 + 1, x1)
            elif(y1 > 1 and map[y1 - 1][x1] == "."):
                empty_cell = (y1 - 1, x1)

    return empty_cell

def choose_target(current_position, map):
    ax = 0
    bx = MAX_X - 1
    ay = 0
    by = MAX_Y - 1
    mid_x = int((MAX_X - 1)/2)
    mid_y = int((MAX_Y - 1)/2)

    if((current_position[1] == 0 and current_position[0] == 0) or \
        (current_position[1] == 0 and current_position[0] == MAX_Y - 1) or\
        (current_position[1] == MAX_X - 1 and current_position[0] == 0) or\
        (current_position[1] == MAX_X - 1 and current_position[0] == MAX_Y - 1) or\
        (current_position[0] == mid_y and current_position[1] == mid_x)):
        ax = 0
        bx = MAX_X - 1
        ay = 0
        by = MAX_Y - 1
    elif(current_position[0] <= mid_y and current_position[1] <= mid_x):
        print("choose from top right", file=sys.stderr)
        ax = mid_x
        bx = MAX_X - 1
        ay = 0
        by = mid_y
    elif(current_position[0] >= mid_y and current_position[1] >= mid_x):
        print("choose from bottom left", file=sys.stderr)
        ax = 0
        bx = mid_x
        ay = mid_y
        by = MAX_Y - 1
    elif(current_position[0] >= mid_y and current_position[1] <= mid_x):
        print("choose from top left", file=sys.stderr)
        ax = 0
        bx = mid_x
        ay = 0
        by = mid_y
    elif(current_position[0] <= mid_y and current_position[1] >= mid_x):
        print("choose from bottom right", file=sys.stderr)
        ax = mid_x
        bx = MAX_X - 1
        ay = mid_y
        by = MAX_Y - 1
    t_x = random.randint(ax, bx)
    t_y = random.randint(ay, by)

    iter = 0
    while(map[t_y][t_x] != "." and iter < 500):
        iter += 1
        t_x = random.randint(ax, bx)
        t_y = random.randint(ay, by)

    return (t_y, t_x)

def calculate_players_scores(map, opponent_count):
    scores = [0] * (opponent_count + 1)
    for row in map:
        for cell in row:
            if(cell == "."):
                pass
            elif(cell == "0" and len(scores) > 1):
                scores[0] += 1
            elif(cell == "1"):
                scores[1] += 1
            elif(cell == "2" and len(scores) > 2):
                scores[2] += 1
            elif(cell == "3" and len(scores) > 3):
                scores[3] += 1
    return scores

opponent_count = int(input())  # Opponent count

# game loop
while 1:
    opponents = []
    map = []

    game_round = int(input())
    # x: Your x position
    # y: Your y position
    # back_in_time_left: Remaining back in time
    x, y, back_in_time_left = [int(i) for i in input().split()]
    current_position = (y, x)

    for i in range(opponent_count):
        # opponent_x: X position of the opponent
        # opponent_y: Y position of the opponent
        # opponent_back_in_time_left: Remaining back in time of the opponent
        opponent_x, opponent_y, opponent_back_in_time_left = [int(j) for j in input().split()]
        opponents.append([opponent_y, opponent_x])

    for i in range(20):
        line = input()  # One line of the map ('.' = free, '0' = you, otherwise the id of the opponent)
        map.append(tuple(line))

    if (not target or current_position == target):
        if(current_position == target):
            print("reached target!", target, file=sys.stderr)
        else:
            print("choosing a new target!", file=sys.stderr)

        target = choose_target(current_position, map)

        print("new target is", target, file=sys.stderr)
        print(target[1], target[0])

    else:
        scores = calculate_players_scores(map, opponent_count)
        print("scores", scores, file=sys.stderr)

        if(sum(scores) > ((MAX_X - 1) * (MAX_Y - 1) * 0.5) and \
            max(scores) > scores[0] and back_in_time_left > 0):
            print("going back in time!", file=sys.stderr)
            print("BACK", 25)

        elif(next_cell_busy(current_position, target, map)):
            print("searching for an empty cell towards", target, current_position, file=sys.stderr)
            temp_target = find_empty_cell(current_position, target, map)

            if(temp_target != target):
                print("found empty cell!", temp_target, file=sys.stderr)
            else:
                print("found no empty cell! pursuing target!", temp_target, file=sys.stderr)

            print(temp_target[1], temp_target[0])
        else:
            print("pursuing the target!", target, file=sys.stderr)
            print(target[1], target[0])
