import re

text = input()

pattern = r'(^|(?<=\s))([a-z0-9]+(?:[._-][a-z0-9]+)*@[a-z]+(?:-[a-z]+)*(?:\.[a-z]+(?:-[a-z]+)*)+)'

matches = re.finditer(pattern, text, flags=re.IGNORECASE)

for m in matches:
    print(m.group(2))