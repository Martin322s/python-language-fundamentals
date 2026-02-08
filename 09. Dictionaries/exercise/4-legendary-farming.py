key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}

legendary = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}

obtained = None

while not obtained:
    parts = input().lower().split()
    for i in range(0, len(parts), 2):
        qty = int(parts[i])
        mat = parts[i + 1]

        if mat in key_materials:
            key_materials[mat] += qty
            if key_materials[mat] >= 250:
                obtained = legendary[mat]
                key_materials[mat] -= 250
                break
        else:
            if mat not in junk:
                junk[mat] = 0
            junk[mat] += qty

print(f"{obtained} obtained!")

for mat in ["shards", "fragments", "motes"]:
    print(f"{mat}: {key_materials[mat]}")

for mat, qty in junk.items():
    print(f"{mat}: {qty}")