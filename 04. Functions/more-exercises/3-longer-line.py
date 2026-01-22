import math

def distance_from_center(x, y):
    return math.sqrt(x * x + y * y)

def line_length(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def closer_point(x1, y1, x2, y2):
    if distance_from_center(x1, y1) <= distance_from_center(x2, y2):
        return (math.floor(x1), math.floor(y1)), (math.floor(x2), math.floor(y2))
    else:
        return (math.floor(x2), math.floor(y2)), (math.floor(x1), math.floor(y1))

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

length1 = line_length(x1, y1, x2, y2)
length2 = line_length(x3, y3, x4, y4)

if length1 >= length2:
    p1, p2 = closer_point(x1, y1, x2, y2)
else:
    p1, p2 = closer_point(x3, y3, x4, y4)

print(f"({p1[0]}, {p1[1]})({p2[0]}, {p2[1]})")