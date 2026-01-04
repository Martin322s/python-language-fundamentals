coffees = 0

while True:
    command = input()
    if command == "END":
        break
    
    lower = command.lower()

    if lower == "coding" or lower == "dog" or lower == "cat" or lower == "movie":
        if command.isupper():
            coffees += 2
        else:
            coffees += 1

if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)