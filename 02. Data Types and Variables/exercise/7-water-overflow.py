capacity = 255
n = int(input())
tank = 0

for _ in range(n):
    liters = int(input())
    if tank + liters > capacity:
        print("Insufficient capacity!")
    else:
        tank += liters

print(tank)