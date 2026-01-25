targets = list(map(int, input().split()))

command = input()

while command != "End":
    parts = command.split()
    action = parts[0]

    if action == "Shoot":
        index = int(parts[1])
        power = int(parts[2])

        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)

    elif action == "Add":
        index = int(parts[1])
        value = int(parts[2])

        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        index = int(parts[1])
        radius = int(parts[2])

        left = index - radius
        right = index + radius

        if left >= 0 and right < len(targets):
            del targets[left:right + 1]
        else:
            print("Strike missed!")

    command = input()

print("|".join(str(x) for x in targets))