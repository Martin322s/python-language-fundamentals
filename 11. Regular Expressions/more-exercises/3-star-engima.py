import re

n = int(input())

attacked = []
destroyed = []

pattern = re.compile(
    r'@(?P<planet>[A-Za-z]+)[^@\-!:>]*'
    r':(?P<population>\d+)[^@\-!:>]*'
    r'!(?P<type>[AD])![^@\-!:>]*'
    r'->(?P<soldiers>\d+)'
)

for _ in range(n):
    encrypted = input()

    key = sum(1 for ch in encrypted.lower() if ch in "star")

    decrypted = "".join(chr(ord(ch) - key) for ch in encrypted)

    match = pattern.search(decrypted)
    if not match:
        continue

    planet = match.group("planet")
    attack_type = match.group("type")

    if attack_type == "A":
        attacked.append(planet)
    elif attack_type == "D":
        destroyed.append(planet)

attacked.sort()
destroyed.sort()

print(f"Attacked planets: {len(attacked)}")
for p in attacked:
    print(f"-> {p}")

print(f"Destroyed planets: {len(destroyed)}")
for p in destroyed:
    print(f"-> {p}")