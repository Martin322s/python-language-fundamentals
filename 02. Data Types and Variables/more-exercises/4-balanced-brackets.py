n = int(input())

last_bracket = ""
balanced = True

for _ in range(n):
    line = input()

    if line == "(":
        if last_bracket == "(":
            balanced = False
        last_bracket = "("

    elif line == ")":
        if last_bracket != "(":
            balanced = False
        last_bracket = ")"

if last_bracket == "(":
    balanced = False

if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")