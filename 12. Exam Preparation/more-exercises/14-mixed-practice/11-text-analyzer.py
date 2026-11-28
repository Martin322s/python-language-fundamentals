import sys

def solve():
    lines = [line.strip() for line in sys.stdin.read().strip().splitlines() if line.strip()]
    for line in lines:
        parts = line.split()
        if len(parts) >= 2:
            try:
                print(f"{parts[0]}: {int(parts[1])}")
            except ValueError:
                print(line)
        else:
            print(line)

if __name__ == "__main__":
    solve()
