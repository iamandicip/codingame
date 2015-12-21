import sys
import math

surface = []
landing_zone = ()
R_I = 45    #rotation increment
P_I = 1     #power increment
MAX_H_SPEED = 20
MAX_V_SPEED = 40
landing_y = 0

def is_close_enough(h_speed, v_speed, x, y):
    close_enough = False

    check_speeds = abs(h_speed) <= MAX_H_SPEED and abs(v_speed) <= MAX_V_SPEED

    check_position = True

    if(landing_zone[0] <= x and x <= landing_zone[1]):
        middle_landing = landing_zone[0] + (landing_zone[1] - landing_zone[0])/2

        if(h_speed < 0 and x < middle_landing):
            check_position = False
        elif(h_speed > 0 and x > middle_landing):
            check_position = False

    close_enough = check_speeds and check_position

    return close_enough

def calculate_angle(x, y, current_angle, h_speed, v_speed):
    result = current_angle

    #calculate if the speed is too big
    speed_too_big = abs(h_speed) >= 3 * MAX_H_SPEED

    #if we are above the landing zone
    if(landing_zone[0] <= x and x <= landing_zone[1]):

        close_enough = is_close_enough(h_speed,v_speed, x, y)

        #if within speed limit, stabilize angle
        if(abs(h_speed) <= MAX_H_SPEED and close_enough):
            result = 0

        #try to slow down if speed is too high
        else:
            #rotate left
            if(h_speed > MAX_H_SPEED or (speed_too_big and h_speed > 0)):
                result = R_I

            #rotate right
            elif(h_speed < -MAX_H_SPEED or (speed_too_big and h_speed < 0)):
                result = -R_I

    #if we are to the left of the landing zone
    elif(x < landing_zone[0]):

        #slow down
        if(speed_too_big and h_speed > 0):
            result = R_I

        #if we are within speed limit, keep vertical
        elif(h_speed > 0 and abs(h_speed) >= MAX_H_SPEED):
            result = 0

        #move to the left
        else:
            result =-R_I

    #if we are to the right of the landing zone
    elif(x > landing_zone[1]):

        #slow down
        if(speed_too_big and h_speed < 0):
            result = - R_I

        #if we are within speed limit, keep vertical
        elif(h_speed < 0 and abs(h_speed) >= MAX_H_SPEED):
            result = 0

        #move to the right
        else:
            result = R_I

    return result

def calculate_thrust(x, y, current_thrust, current_angle, v_speed, h_speed):
    result = current_thrust

    #don't get too high
    if(current_thrust == 4 and v_speed > 0):
        result = current_thrust - P_I
        return result

    above_landing_zone = landing_zone[0] <= x and x <= landing_zone[1]

    #keep full thrust while not above a landing zone
    if(not above_landing_zone):
        if(current_thrust + P_I <= 4):
            result = current_thrust + P_I
    else:
        #thrust if not angle of horizontal speed not stable
        if ((current_angle < 0 and h_speed < MAX_H_SPEED)
            or (current_angle > 0 and h_speed > -MAX_H_SPEED)):
            if(current_thrust + P_I <= 4):
                result = current_thrust + P_I

        #stabilize vertical speed
        elif(current_angle == 0):

            #calculate if we should reduce the thrust
            close_enough = is_close_enough(h_speed, v_speed, x, y)

            #thrust if descending too fast
            if(abs(v_speed) >= MAX_V_SPEED or not close_enough):
                if(current_thrust + P_I <= 4):
                    result = current_thrust + P_I

            #reduce thrust to land as long as you don't descend too fast
            elif(close_enough and abs(v_speed)/MAX_V_SPEED < 0.5):
                if(current_thrust - P_I >= 0):
                    result = current_thrust - P_I

    return result

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    surface.append((land_x, land_y))

#identify the flat surfaces
for i in range(surface_n - 1):
    if(surface[i][1] == surface[i+1][1]):
        landing_zone += ((surface[i][0], surface[i+1][0]))
        landing_y = surface[i][1]

# game loop
while 1:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    desired_rotate = calculate_angle(x, y, rotate, h_speed, v_speed)

    desired_power = calculate_thrust(x, y, power, rotate, v_speed, h_speed)

    # rotate power. rotate is the desired rotation angle. power is the desired thrust power.
    print(desired_rotate, desired_power)
