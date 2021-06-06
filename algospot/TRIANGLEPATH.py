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

# 풀이 참고 limdongjin님 코드


import sys
input = sys.stdin.readline
def path(board, n):
    dp = [[-1]*(n+1) for _ in range(n+1)]
    
    def _path(y, x):
        if y == n - 1:
            return board[y][x]
        if dp[y][x] != -1:
            return dp[y][x]

        dp[y][x] = board[y][x] + max(_path(y+1, x), _path(y+1, x+1))
        return dp[y][x]

    return _path(y=0,x=0)
c = int(input())
board = [[0]*101 for _ in range(101)]
for _ in range(c):
    n  = int(input())
    for y in range(n):
        line = list(map(int, input().split()))
        for x in range(y+1):
            board[y][x] = line[x]

    print(path(board, n))
