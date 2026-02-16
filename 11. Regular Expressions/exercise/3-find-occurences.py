import re

word = input()
sentence = input()

pattern = rf'(?i)(?<![A-Za-z]){re.escape(word)}(?![A-Za-z])'

matches = re.findall(pattern, sentence)
print(len(matches))