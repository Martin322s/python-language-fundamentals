a = int(input())
b = int(input())
c = int(input())

if a == 0 or b == 0 or c == 0:
    print("zero")
else:
    negatives = 0

    if a < 0:
        negatives += 1
    if b < 0:
        negatives += 1
    if c < 0:
        negatives += 1

    if negatives % 2 == 0:
        print("positive")
    else:
        print("negative")