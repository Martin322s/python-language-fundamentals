n = int(input())

best_value = 0
best_snow = 0
best_time = 0
best_quality = 0

for _ in range(n):
    snow = int(input())
    time = int(input())
    quality = int(input())

    value = (snow // time) ** quality

    if value > best_value:
        best_value = value
        best_snow = snow
        best_time = time
        best_quality = quality

print(f"{best_snow} : {best_time} = {best_value} ({best_quality})")