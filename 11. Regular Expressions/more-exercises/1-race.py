import re

participants = input().split(", ")
distances = {name: 0 for name in participants}

name_pattern = r"[A-Za-z]"
digit_pattern = r"\d"

while True:
    line = input()
    if line == "end of race":
        break

    name = "".join(re.findall(name_pattern, line))
    distance = sum(int(x) for x in re.findall(digit_pattern, line))

    if name in distances:
        distances[name] += distance

top3 = sorted(distances.items(), key=lambda x: -x[1])[:3]

print(f"1st place: {top3[0][0]}")
print(f"2nd place: {top3[1][0]}")
print(f"3rd place: {top3[2][0]}")