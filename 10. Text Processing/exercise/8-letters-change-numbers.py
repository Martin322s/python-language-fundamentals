data = input().split()

total_sum = 0.0

for token in data:
    first_letter = token[0]
    last_letter = token[-1]
    number = int(token[1:-1])

    first_pos = ord(first_letter.lower()) - ord('a') + 1
    last_pos = ord(last_letter.lower()) - ord('a') + 1

    if first_letter.isupper():
        result = number / first_pos
    else:
        result = number * first_pos

    if last_letter.isupper():
        result -= last_pos
    else:
        result += last_pos

    total_sum += result

print(f"{total_sum:.2f}")