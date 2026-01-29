def solve():
    n = int(input())
    maze = [list(input()) for _ in range(n)]

    start_row = start_col = None
    for r in range(n):
        for c in range(len(maze[r])):
            if maze[r][c] == "k":
                start_row, start_col = r, c
                break
        if start_row is not None:
            break

    visited = set()

    def is_exit(r, c):
        return r == 0 or r == n - 1 or c == 0 or c == len(maze[r]) - 1

    def dfs(r, c):
        if (r, c) in visited:
            return -1
        visited.add((r, c))
        
        if is_exit(r, c):
            return 0

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < n and 0 <= nc < len(maze[nr]):
                if maze[nr][nc] == " ":
                    moves = dfs(nr, nc)
                    if moves != -1:
                        return moves + 1

        return -1

    result = dfs(start_row, start_col)

    if result == -1:
        print("Kate cannot get out")
    else:
        print(f"Kate got out in {result} moves")
        
solve()