contests = {}              
contest_user_order = {}     
user_total = {}             
user_first_seen = {}        
global_idx = 0             


while True:
    line = input()
    if line == "no more time":
        break

    username, contest, pts_str = line.split(" -> ")
    points = int(pts_str)

    if username not in user_first_seen:
        user_first_seen[username] = global_idx
    global_idx += 1

    if contest not in contests:
        contests[contest] = {}
        contest_user_order[contest] = {}

    if username not in contest_user_order[contest]:
        contest_user_order[contest][username] = len(contest_user_order[contest])

    if username not in contests[contest]:
        contests[contest][username] = points
        user_total[username] = user_total.get(username, 0) + points
    else:
        old_points = contests[contest][username]
        if points > old_points:
            contests[contest][username] = points
            user_total[username] += (points - old_points)

for contest_name, participants in contests.items():
    print(f"{contest_name}: {len(participants)} participants")

    sorted_participants = sorted(
        participants.items(),
        key=lambda x: (-x[1], x[0], contest_user_order[contest_name][x[0]])
    )

    for pos, (user, pts) in enumerate(sorted_participants, start=1):
        print(f"{pos}. {user} <::> {pts}")

print("Individual standings:")

sorted_users = sorted(
    user_total.items(),
    key=lambda x: (-x[1], x[0], user_first_seen[x[0]])
)

for pos, (user, total_pts) in enumerate(sorted_users, start=1):
    print(f"{pos}. {user} -> {total_pts}")