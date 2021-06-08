
# 입력
# 4
# 5 4
# 5 3
# 4 2
# 3 2

# 출력
# 0.9960937500
# 0.8437500000
# 0.5625000000
# 0.9375000000


#chacham님 코드 참고
import sys
sys.setrecursionlimit(10000)

dp = [[-1] * (1001) for _ in range(1001)]
for i in range(1001):
    dp[i][0] = 0
    dp[i][1] = 0
for i in range(1001):
    dp[0][i] = 1
    dp[1][i] = 1
dp[0][0], dp[0][1] = 1, 1
dp[1][0], dp[1][1] = 0, 1
dp[2][1] = 0.75

def climb(N, M):
    def rec(restHeight, restDays):
        if dp[restHeight][restDays] != -1:
            return dp[restHeight][restDays]
        if restDays == 0:
            return 1 if restHeight <= 0 else 0
        if restHeight <= restDays:
            return 1
        dp[restHeight][restDays] = rec(restHeight-2, restDays-1) * 0.75 + rec(restHeight-1, restDays-1) * 0.25
        return dp[restHeight][restDays]
    return rec(N, M)


for _ in range(int(input())):

    n, m = sys.stdin.readline().strip().split()
    n, m = int(n), int(m) # depth, days

    print(format(climb(n, m), ".10f"))
