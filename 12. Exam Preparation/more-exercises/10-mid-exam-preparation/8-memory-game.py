import sys

def solve():
    lines = sys.stdin.read().strip().splitlines()
    numbers = [int(value) for value in lines[0].split()] if lines else []
    for line in lines[1:]:
        parts = line.split()
        if not parts:
            continue
        command = parts[0]
        if command == "Swap" and len(parts) == 3:
            i, j = int(parts[1]), int(parts[2])
            if 0 <= i < len(numbers) and 0 <= j < len(numbers):
                numbers[i], numbers[j] = numbers[j], numbers[i]
        elif command == "Multiply" and len(parts) == 3:
            i, j = int(parts[1]), int(parts[2])
            if 0 <= i < len(numbers) and 0 <= j < len(numbers):
                numbers[i] *= numbers[j]
        elif command == "Decrease":
            numbers = [value - 1 for value in numbers]
    print(" | ".join(str(value) for value in numbers))

if __name__ == "__main__":
    solve()
