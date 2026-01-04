line = input()

animals = line.split(", ")

wolf_index = 0

i = 0
while i < len(animals):
    if animals[i] == "wolf":
        wolf_index = i
        break
    i += 1

if wolf_index == len(animals) - 1:
    print("Please go away and stop eating my sheep")
else:
    sheep_number = len(animals) - wolf_index - 1
    print("Oi! Sheep number " + str(sheep_number) + "! You are about to be eaten by a wolf!")