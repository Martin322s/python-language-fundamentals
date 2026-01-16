numbers = input().split()
text = list(input())

message = ""

for num in numbers:
    digit_sum = sum(int(d) for d in num)

    index = digit_sum % len(text)

    message += text[index]

    text.pop(index)

print(message)