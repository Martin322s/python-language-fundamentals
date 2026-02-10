force_sides = {}

def find_user(user):
    for side, users in force_sides.items():
        if user in users:
            return side
    return None

while True:
    command = input()
    if command == "Lumpawaroo":
        break

    if " | " in command:
        side, user = command.split(" | ")

        if side not in force_sides:
            force_sides[side] = []

        if not find_user(user):
            force_sides[side].append(user)

    else:
        user, side = command.split(" -> ")

        if side not in force_sides:
            force_sides[side] = []

        old_side = find_user(user)
        if old_side:
            force_sides[old_side].remove(user)

        force_sides[side].append(user)
        print(f"{user} joins the {side} side!")

filtered = {s: u for s, u in force_sides.items() if u}

sorted_sides = sorted(filtered.items(), key=lambda x: -len(x[1]))

for side, users in sorted_sides:
    print(f"Side: {side}, Members: {len(users)}")

    for user in sorted(users, reverse=True):
        print(f"! {user}")