import sys

def solve():
    rows = []
    for line in sys.stdin.read().strip().splitlines():
        numbers = [int(value) for value in line.split() if value.lstrip("-").isdigit()]
        if numbers:
            rows.append(numbers)
    flat = [value for row in rows for value in row]
    print(" ".join(str(value) for value in flat))

if __name__ == "__main__":
    solve()
