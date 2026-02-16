import re

regex = r"\b[A-Z][a-z]+\b \b[A-Z][a-z]+\b"

names = input()

result = re.findall(regex, names)

print(*result)