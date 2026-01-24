words = input().split()
decoded = []

for word in words:
    digits = ""
    rest = ""
    for ch in word:
        if ch.isdigit():
            digits += ch
        else:
            rest += ch

    first_letter = chr(int(digits))

    if len(rest) > 1:
        rest = rest[-1] + rest[1:-1] + rest[0]

    decoded.append(first_letter + rest)

print(" ".join(decoded))
