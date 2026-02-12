contests = {}

while True:
    line = input()
    if line == "end of contests":
        break
    contest, password = line.split(":")
    contests[contest] = password

users = {}

while True:
    line = input()
    if line == "end of submissions":
        break

    contest, password, username, points_str = line.split("=>")
    points = int(points_str)

    if contest not in contests:
        continue
    if contests[contest] != password:
        continue

    if username not in users:
        users[username] = {}

    if contest not in users[username]:
        users[username][contest] = points
    else:
        if points > users[username][contest]:
            users[username][contest] = points

best_user = None
best_total = 0

for username, contests_points in users.items():
    total_points = sum(contests_points.values())
    if total_points > best_total:
        best_total = total_points
        best_user = username

print(f"Best candidate is {best_user} with total {best_total} points.")

print("Ranking:")

for username in sorted(users.keys()):
    print(username)
    
    sorted_contests = sorted(users[username].items(), key=lambda x: -x[1])
    for contest, pts in sorted_contests:
        print(f"#  {contest} -> {pts}")