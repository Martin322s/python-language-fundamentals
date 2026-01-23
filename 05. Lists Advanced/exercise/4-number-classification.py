numbers = list(map(int, input().split(", ")))

positives = [n for n in numbers if n >= 0]
negatives = [n for n in numbers if n < 0]
evens = [n for n in numbers if n % 2 == 0]
odds = [n for n in numbers if n % 2 != 0]

print(f"Positive: {positives}")
print(f"Negative: {negatives}")
print(f"Even: {evens}")
print(f"Odd: {odds}")