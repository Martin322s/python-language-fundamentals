text = input()

t = text.lower()

count = 0

i = 0
while i < len(t):
    if t[i:i+4] == "sand":
        count += 1
    if t[i:i+5] == "water":
        count += 1
    if t[i:i+4] == "fish":
        count += 1
    if t[i:i+3] == "sun":
        count += 1
    i += 1

print(count)