text = input()
result = ""

for index in range(0, len(text)):
	result = result + text[index] + text[index]

print(result)