import sys

def solve():
    counts = {}
    for value in sys.stdin.read().split():
        counts[value] = counts.get(value, 0) + 1
    for key, value in counts.items():
        print(f"{key} -> {value}")

if __name__ == "__main__":
    solve()
