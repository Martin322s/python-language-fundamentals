import sys

def solve():
    values = [int(value) for value in sys.stdin.read().split() if value.lstrip("-").isdigit()]
    print(" ".join(str(value) for value in sorted(set(values))))

if __name__ == "__main__":
    solve()
