text = input()
capitals = []

for i in range(0, len(text)):
	if text[i].isupper():
		capitals.append(i)

print(capitals)