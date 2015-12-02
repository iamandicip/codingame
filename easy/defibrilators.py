import sys
import math

defibs = []
attr_names = ("number","name","address","phone","long","lat")

def get_distance(source, target):
    s_lat = source[0]
    s_long = source[1]
    t_lat = target[0]
    t_long = target[1]
    
    x = (t_long - s_long) * math.cos((t_lat + s_lat)/2)
    y = t_lat - s_lat
    
    d = math.sqrt((x * x) + (y * y)) * 6371
    
    return d

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = input()
lat = input()

lon = float(lon.replace(",", "."))
lat = float(lat.replace(",", "."))
current_position = (lat, lon)

n = int(input())
for i in range(n):
    defib = input()
    
    current_defib = {}
    
    attr_values = defib.split(";");
    for j in range (len(attr_names)):
        key = attr_names[j]
        value = attr_values[j]

        if(key == "long" or key == "lat"):
            value = float(value.replace(",", "."))

        current_defib[key] = value
        
    defibs.append(current_defib)
    
print(defibs, file=sys.stderr)

minimum_distance = sys.maxsize
closest_defib = ""

for i in range(len(defibs)):
    current_defib = defibs[i]
    defib_position = (current_defib["lat"], current_defib["long"])

    d = get_distance(current_position, defib_position)

    if(d <= minimum_distance):
        minimum_distance = d
        closest_defib = current_defib["name"]

print(closest_defib)
