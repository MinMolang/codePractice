
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

# Courier님 코드 참고

import sys

# 소수점 10자리 처리
def climb(n, m):
    if n <= 0:
        return 1.
    if m == 0:
        return 0.
    if dp[n - 1][m - 1] is None:
        dp[n -1][m - 1] = (0.25 * climb(n - 1, m - 1)) + (0.75 * climb(n - 2, m - 1))
    return dp[n -1][m - 1]



for _ in range(int(input())):
    # H,W 입력
    n, m = sys.stdin.readline().strip().split()
    n, m = int(n), int(m) # depth, days

    dp = [[None] * 1000 for _ in range(1000)] # dp[n][m] n,m <= 1000
    print(format(climb(n, m), ".10f"))
