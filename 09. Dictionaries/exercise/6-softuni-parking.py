n = int(input())
parking = {}

for _ in range(n):
    command = input().split()

    if command[0] == "register":
        user = command[1]
        plate = command[2]
        if user in parking:
            print(f"ERROR: already registered with plate number {parking[user]}")
        else:
            parking[user] = plate
            print(f"{user} registered {plate} successfully")

    else:
        user = command[1]
        if user not in parking:
            print(f"ERROR: user {user} not found")
        else:
            del parking[user]
            print(f"{user} unregistered successfully")

for user, plate in parking.items():
    print(f"{user} => {plate}")