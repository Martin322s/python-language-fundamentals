import re

pattern = r'(^|(?<=\s))-?(0|[1-9]\d*)(\.\d+)?(?=$|\s)'
text = input()

matches = re.finditer(pattern, text)

result = [m.group() for m in matches]
print(" ".join(result))