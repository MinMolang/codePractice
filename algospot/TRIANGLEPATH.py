# 2
# 5
# 6
# 1  2
# 3  7  4
# 9  4  1  7
# 2  7  5  9  4
# 5
# 1
# 2 4
# 8 16 8
# 32 64 32 64
# 128 256 128 256 128
#
# 28
# 341

# 6
# 1  2
# 3  7  4
# 9  4  1  7
# 2  7  5  9  4
# 의 경우 6 + 2 + 4 + 7 + 9

# 풀이 참고 https://hellominchan.tistory.com/239
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



