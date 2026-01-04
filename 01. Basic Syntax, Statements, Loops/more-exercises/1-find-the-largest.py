s = input()
result = ""

while len(s) > 0:
    max_digit = "0"
    max_index = 0

    i = 0
    while i < len(s):
        if s[i] > max_digit:
            max_digit = s[i]
            max_index = i
        i += 1

    result += max_digit

    s = s[:max_index] + s[max_index+1:]

print(result)