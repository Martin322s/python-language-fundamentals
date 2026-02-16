import re

regex_emoji = r"(?P<surrounder>::|\*\*)(?P<text>[A-Z][a-z]{2,})\1"
regex_digits = r"\d"

text = input()

digits = [int(x) for x in re.findall(regex_digits, text)]
matches = list(re.finditer(regex_emoji, text))

cool_threshold = 1
for d in digits:
    cool_threshold *= d

cool_emojis = []

for m in matches:
    emoji_text = m.group("text")
    coolness = sum(ord(ch) for ch in emoji_text)
    if coolness > cool_threshold:
        cool_emojis.append(m.group(0))

print(f"Cool threshold: {cool_threshold}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")
print("\n".join(cool_emojis))