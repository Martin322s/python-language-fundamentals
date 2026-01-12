gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break

    parts = command.split()
    action = parts[0]

    if action == "OutOfStock":
        gift = parts[1]
        for i in range(len(gifts)):
            if gifts[i] == gift:
                gifts[i] = "None"

    elif action == "Required":
        gift = parts[1]
        index = int(parts[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift

    elif action == "JustInCase":
        gift = parts[1]
        gifts[-1] = gift

result = [g for g in gifts if g != "None"]

print(" ".join(result))
