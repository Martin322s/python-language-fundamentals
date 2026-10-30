import sys

def solve():
    values = sys.stdin.read().strip().split()
    integers = [int(value) for value in values if value.lstrip("-").isdigit()]
    print(sum(integers))

if __name__ == "__main__":
    solve()
