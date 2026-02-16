text = input()

result = []
strength = 0

for i in range(len(text)):
    char = text[i]

    if char == ">":
        result.append(char)
        strength += int(text[i + 1])
    elif strength > 0:
        strength -= 1
    else:
        result.append(char)

print("".join(result))