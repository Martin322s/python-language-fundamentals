import sys

def solve():
    numbers = [int(value) for value in sys.stdin.read().split() if value.lstrip("-").isdigit()]
    if not numbers:
        print("No numbers")
        return
    print(max(numbers))

if __name__ == "__main__":
    solve()
