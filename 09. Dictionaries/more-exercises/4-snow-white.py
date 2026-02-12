dwarfs = {}      
first_seen = {}  
idx = 0

while True:
    line = input()
    if line == "Once upon a time":
        break

    name, color, phys_str = line.split(" <:> ")
    physics = int(phys_str)

    key = (name, color)

    if key not in dwarfs:
        dwarfs[key] = physics
        first_seen[key] = idx
        idx += 1
    else:
        if physics > dwarfs[key]:
            dwarfs[key] = physics

color_count = {}
for (name, color) in dwarfs.keys():
    color_count[color] = color_count.get(color, 0) + 1

sorted_dwarfs = sorted(
    dwarfs.items(),
    key=lambda item: (
        -item[1],                               
        -color_count[item[0][1]],                
        first_seen[item[0]]                      
    )
)

for (name, color), physics in sorted_dwarfs:
    print(f"({color}) {name} <-> {physics}")
