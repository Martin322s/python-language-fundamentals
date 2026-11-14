import re
import sys

def solve():
    matches = re.findall(r"-?\d+(?:\.\d+)?", sys.stdin.read())
    print(" ".join(matches))

if __name__ == "__main__":
    solve()
