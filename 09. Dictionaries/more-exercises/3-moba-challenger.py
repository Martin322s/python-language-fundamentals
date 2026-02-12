players = {}

while True:
    line = input()
    if line == "Season end":
        break

    if " -> " in line:
        player, position, skill_str = line.split(" -> ")
        skill = int(skill_str)

        if player not in players:
            players[player] = {}

        if position not in players[player]:
            players[player][position] = skill
        else:
            if skill > players[player][position]:
                players[player][position] = skill

    else:
        p1, p2 = line.split(" vs ")

        if p1 in players and p2 in players:
            positions1 = set(players[p1].keys())
            positions2 = set(players[p2].keys())
            common = positions1 & positions2

            if common:
                total1 = sum(players[p1].values())
                total2 = sum(players[p2].values())

                if total1 > total2:
                    del players[p2]
                elif total2 > total1:
                    del players[p1]

def total_skill(player_dict):
    return sum(player_dict.values())

sorted_players = sorted(
    players.items(),
    key=lambda x: (-total_skill(x[1]), x[0])
)

for player, pos_dict in sorted_players:
    print(f"{player}: {total_skill(pos_dict)} skill")

    sorted_positions = sorted(
        pos_dict.items(),
        key=lambda x: (-x[1], x[0])
    )

    for position, skill in sorted_positions:
        print(f"- {position} <::> {skill}")