text = input()

counts = {}
for ch in text:
    if ch == " ":
        continue
    counts[ch] = counts.get(ch, 0) + 1

for ch, cnt in counts.items():
    print(f"{ch} -> {cnt}")