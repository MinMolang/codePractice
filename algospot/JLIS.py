#py3는 시간초과나서 pypy2로 

# 입력
# 3
# 3 3
# 1 2 4
# 3 4 7
# 3 3
# 1 2 3
# 4 5 6
# 5 3
# 10 20 30 1 2
# 10 20 30

# 출력
# 5
# 6
# 5

# 코드 출처 : only123님 풀이


import sys

MIN = -3000000000


def Jlis():
    for ai in reversed(xrange(-1, lis_lenA)):
        for bi in reversed(xrange(-1, lis_lenB)):
            a = MIN if ai == -1 else sequenceA[ai]
            b = MIN if bi == -1 else sequenceB[bi]
            maxVal = max(a, b)

            ret = 0
            for i in xrange(ai + 1, lis_lenA):
                if maxVal < sequenceA[i]:
                    val = dp[i + 1][bi + 1] + 1
                    ret = max(ret, val)
            for i in xrange(bi + 1, lis_lenB):
                if maxVal < sequenceB[i]:
                    val = dp[ai + 1][i + 1] + 1
                    ret = max(ret, val)
            dp[ai + 1][bi + 1] = ret
    return dp[0][0]


rl = lambda: sys.stdin.readline()

for _ in xrange(input()):

    lis_lenA, lis_lenB = map(int, rl().split())
    sequenceA = map(int, rl().split())
    sequenceB = list(map(int, rl().split()))


    dp = [[0] * (lis_lenB + 1) for _ in xrange(lis_lenA + 1)]


    print Jlis()


