numbers = list(map(int, input().split()))
n = int(input())

for _ in range(n):
    smallest = min(numbers)
    numbers.remove(smallest)

print(", ".join(map(str, numbers)))