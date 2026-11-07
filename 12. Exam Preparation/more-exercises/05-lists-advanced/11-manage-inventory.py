import sys

def solve():
    values = [value for value in sys.stdin.read().split()]
    print(" ".join(sorted(set(values))))

if __name__ == "__main__":
    solve()
