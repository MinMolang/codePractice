# 입력
# 2
# 7
# 2 5 1 6 1 4 1
# 6 1 1 2 2 9 3
# 7 2 3 2 1 3 1
# 1 1 3 1 7 1 2
# 4 1 2 3 4 1 2
# 3 3 1 2 3 4 1
# 1 5 2 9 4 7 0
# 7
# 2 5 1 6 1 4 1
# 6 1 1 2 2 9 3
# 7 2 3 2 1 3 1
# 1 1 3 1 7 1 2
# 4 1 2 3 4 1 3
# 3 3 1 2 3 4 1
# 1 5 2 9 4 7 0

#출력
# YES
# NO

# 풀이 참고 : https://hellominchan.tistory.com/267

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# 우측으로 이동, 아래로 이동
# 메모활용
def move(i, j):
    if i > N - 1 or j > N - 1:
        return 0
    if i == N - 1 and j == N - 1:
        return 1

    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = move(i + board[i][j], j) or move(i, j + board[i][j])

    return dp[i][j]

for _ in range(int(input())):
    N =  int(input())
    board = [ list(map(int, input().split())) for _ in range(N)]
    dp = [[-1] * N for _ in range(N)]
    print('YES' if move(0, 0) else 'NO')
