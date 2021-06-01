
import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                board[i][j] += board[i - 1][j]
            elif j == i:
                board[i][j] += board[i - 1][j - 1]
            else:
                board[i][j] += max(board[i - 1][j], board[i - 1][j - 1])

    print(max(board[-1]))
