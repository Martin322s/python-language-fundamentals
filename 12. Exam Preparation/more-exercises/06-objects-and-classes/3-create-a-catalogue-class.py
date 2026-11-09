import sys

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def solve():
    lines = sys.stdin.read().strip().splitlines()
    items = []
    for line in lines:
        parts = line.split()
        if len(parts) >= 2:
            try:
                items.append(Item(parts[0], int(parts[1])))
            except ValueError:
                continue
    print(" ".join(item.name for item in sorted(items, key=lambda item: item.value)))

if __name__ == "__main__":
    solve()
