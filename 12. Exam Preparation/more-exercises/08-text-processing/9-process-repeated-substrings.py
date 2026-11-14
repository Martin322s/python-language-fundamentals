import sys

def solve():
    text = sys.stdin.read().strip()
    print(text[::-1])

if __name__ == "__main__":
    solve()
