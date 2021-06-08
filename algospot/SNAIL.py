
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

# 책 풀이법 + c++풀이 참고(https://jaimemin.tistory.com/326)

import sys

# 소수점 10자리 처리
def climb(passed, climbed):
    global n,m
    # 기저사례 : days가 모두 지나간 경우
    if passed == m:
        return 1 if climbed >= n else 0

    # 메모이제이션
    ret = dp[passed][climbed]
    if ret != -1.0: # 이미 방문한 경우
        return ret

    ret = (0.25 * climb(passed + 1, climbed + 1)) + (0.75 * climb(passed + 1, climbed + 2))
    return ret



for _ in range(int(input())):
    # H,W 입력
    n, m = sys.stdin.readline().strip().split()
    n, m = int(n), int(m) # depth, days

    dp = [[-1.0] * (2*m+1) for _ in range(m+1)] # dp[passed days][climbed depth] 우물을 오를 수 있는 높이는 최대 2m * 일자
    print(format(climb(0, 0), ".10f"))