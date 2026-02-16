import re

line = input()

demons = [d for d in re.split(r'\s*,\s*', line.strip()) if d]

result = {}

for demon in demons:
    health_chars = re.findall(r'[^0-9+\-*/.]', demon)
    health = sum(ord(ch) for ch in health_chars)

    numbers = re.findall(r'[+\-]?\d+(?:\.\d+)?', demon)
    damage = sum(float(num) for num in numbers) if numbers else 0.0

    for ch in demon:
        if ch == '*':
            damage *= 2
        elif ch == '/':
            damage /= 2

    result[demon] = (health, damage)

for name in sorted(result.keys()):
    h, d = result[name]
    print(f"{name} - {h} health, {d:.2f} damage")