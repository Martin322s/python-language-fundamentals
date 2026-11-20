import sys

def solve():
    lines = sys.stdin.read().strip().splitlines()
    if not lines:
        return
    value = lines[0]
    for line in lines[1:]:
        if line == "Generate":
            break
        parts = line.split(">>>")
        command = parts[0]
        if command == "Contains" and len(parts) == 2:
            print("Substring found" if parts[1] in value else "Substring not found")
        elif command == "Slice" and len(parts) == 3:
            start, end = int(parts[1]), int(parts[2])
            value = value[:start] + value[end:]
        elif command == "Flip" and len(parts) == 4:
            state, start, end = parts[1], int(parts[2]), int(parts[3])
            changed = value[start:end].upper() if state == "Upper" else value[start:end].lower()
            value = value[:start] + changed + value[end:]
    print(f"Result: {value}")

if __name__ == "__main__":
    solve()
