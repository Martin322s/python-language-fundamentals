import sys

def total(values):
    return sum(values)

def solve():
    values = [int(value) for value in sys.stdin.read().split() if value.lstrip("-").isdigit()]
    print(total(values))

if __name__ == "__main__":
    solve()
