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

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# 우측으로 이동, 아래로 이동
# 메모활용
def move(i, j):
    if i > N - 1 or j > N - 1:
        return 0

    if i == N - 1 and dp[i][j] != -1:
        return dp[i][j]

    if dp[i][j] != -1:
        return dp[i][j]

    ret = 0
    dp[i][j] = max(ret, move(i + 1, j), move(i + 1, j + 1))
    ret =   dp[i][j]
    return dp[i][j]

for _ in range(int(input())):
    N =  int(input())
    board = [ list(map(int, input().split())) for _ in range(N)]
    dp = [[-1] * N for _ in range(N)]
    print(move(0, 0))