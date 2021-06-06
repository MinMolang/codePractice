#입력 
# 3
# 2
# 4
# 92

#출력
# 0
# 2
# 913227494
#코드풀이 참고 sanghyun.lee


import sys

dp = []
MOD = 1000000007


def Tiling(n):
    n = int(n)
    if n <= 1:
        return 1

    ret = dp[n]
    if ret != -1:
        return ret

    ret = (Tiling(n - 1) + Tiling(n - 2)) % MOD
    dp[n] = ret
    return ret


def asymmetric(n):
    if (n % 2) == 1: # 홀수 방법 
        return (Tiling(n) - Tiling(n / 2) + MOD) % MOD

    ret = Tiling(n)
    ret = (ret - Tiling(n / 2) + MOD) % MOD # 짝수방법 1) 
    ret = (ret - Tiling(n / 2 - 1) + MOD) % MOD # 짝수 방법 2) 

    return ret


if __name__ == "__main__":
    test_case = int(sys.stdin.readline())

    for i in range(test_case):
        count = int(sys.stdin.readline())
        dp = [-1 for i in range(count + 1)]
        print(asymmetric(count))


