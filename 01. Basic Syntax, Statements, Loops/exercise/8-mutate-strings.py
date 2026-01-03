a = input()
b = input()

current = a

for i in range(len(a)):
    if current[i] != b[i]:
        current = current[:i] + b[i] + current[i+1:]
        print(current)