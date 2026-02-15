n = int(input())

DEFAULT_DAMAGE = 45
DEFAULT_HEALTH = 250
DEFAULT_ARMOR = 10

dragons = {}

for _ in range(n):
    d_type, name, dmg_s, hp_s, arm_s = input().split()

    damage = DEFAULT_DAMAGE if dmg_s == "null" else int(dmg_s)
    health = DEFAULT_HEALTH if hp_s == "null" else int(hp_s)
    armor = DEFAULT_ARMOR if arm_s == "null" else int(arm_s)

    if d_type not in dragons:
        dragons[d_type] = {}

    dragons[d_type][name] = (damage, health, armor)

for d_type, names_dict in dragons.items():
    values = list(names_dict.values())
    count = len(values)

    avg_damage = sum(v[0] for v in values) / count
    avg_health = sum(v[1] for v in values) / count
    avg_armor = sum(v[2] for v in values) / count

    print(f"{d_type}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")

    for name in sorted(names_dict.keys()):
        damage, health, armor = names_dict[name]
        print(f"-{name} -> damage: {damage}, health: {health}, armor: {armor}")