import sys

def solve():
    text = sys.stdin.read().strip()
    if not text:
        print("Invalid input")
        return
    values = []
    for value in text.split():
        try:
            values.append(int(value))
        except ValueError:
            continue
    if not values:
        print("Invalid input")
        return
    print(sum(values))

if __name__ == "__main__":
    solve()
