def solve():
    n = int(input())
    board = [input().split() for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    def dfs(r, c):
        stack = [(r, c)]
        visited[r][c] = True
        size = 0

        while stack:
            x, y = stack.pop()
            size += 1

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if not visited[nx][ny] and board[nx][ny] == '.':
                        visited[nx][ny] = True
                        stack.append((nx, ny))
        return size

    best = 0
    for r in range(n):
        for c in range(n):
            if board[r][c] == '.' and not visited[r][c]:
                best = max(best, dfs(r, c))

    print(best)


solve()