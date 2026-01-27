notes = [0] * 10

command = input()

while command != "End":
    importance_str, note = command.split("-")
    importance = int(importance_str)

    notes.pop(importance - 1)
    notes.insert(importance - 1, note)

    command = input()

result = [n for n in notes if n != 0]

print(result)