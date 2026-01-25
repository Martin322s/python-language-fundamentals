neighborhood = list(map(int, input().split("@")))
position = 0

while True:
    command = input()
    if command == "Love!":
        break

    _, length = command.split()
    length = int(length)

    position += length
    if position >= len(neighborhood):
        position = 0

    if neighborhood[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        neighborhood[position] -= 2
        if neighborhood[position] == 0:
            print(f"Place {position} has Valentine's day.")

print(f"Cupid's last position was {position}.")

failed_places = sum(1 for x in neighborhood if x > 0)

if failed_places == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {failed_places} places.")