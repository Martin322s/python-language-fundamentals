text = input()

for i in range(len(text) - 1):
    if text[i] == ":":
        print(text[i] + text[i + 1])