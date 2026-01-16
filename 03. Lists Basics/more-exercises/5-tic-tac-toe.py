row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
row3 = list(map(int, input().split()))

board = [row1, row2, row3]

winner = 0

for r in board:
    if r[0] == r[1] == r[2] != 0:
        winner = r[0]

for c in range(3):
    if board[0][c] == board[1][c] == board[2][c] != 0:
        winner = board[0][c]

if board[0][0] == board[1][1] == board[2][2] != 0:
    winner = board[0][0]

if board[0][2] == board[1][1] == board[2][0] != 0:
    winner = board[0][2]

if winner == 1:
    print("First player won")
elif winner == 2:
    print("Second player won")
else:
    print("Draw!")