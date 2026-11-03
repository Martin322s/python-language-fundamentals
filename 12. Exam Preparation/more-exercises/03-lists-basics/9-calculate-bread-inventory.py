import sys

def solve():
    values = sys.stdin.read().strip().split()
    numbers = [int(value) for value in values if value.lstrip("-").isdigit()]
    print(" ".join(str(value) for value in reversed(numbers)))

if __name__ == "__main__":
    solve()
