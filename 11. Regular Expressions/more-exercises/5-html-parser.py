import re

html = input()

title_match = re.search(r'<title>(.*?)</title>', html, re.DOTALL)
title = title_match.group(1)

body_match = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
body = body_match.group(1)

title_clean = re.sub(r'<.*?>', '', title)
body_clean = re.sub(r'<.*?>', '', body)

title_clean = title_clean.replace("\\n", " ")
body_clean = body_clean.replace("\\n", " ")

title_clean = re.sub(r'\s+', ' ', title_clean).strip()
body_clean = re.sub(r'\s+', ' ', body_clean).strip()

print(f"Title: {title_clean}")
print(f"Content: {body_clean}")