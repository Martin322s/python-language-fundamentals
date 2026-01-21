import math

def distance_from_center(x, y):
    return math.sqrt(x * x + y * y)

def closer_point(x1, y1, x2, y2):
    d1 = distance_from_center(x1, y1)
    d2 = distance_from_center(x2, y2)

    if d1 <= d2:
        return math.floor(x1), math.floor(y1)
    else:
        return math.floor(x2), math.floor(y2)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

cx, cy = closer_point(x1, y1, x2, y2)
print(f"({cx}, {cy})")