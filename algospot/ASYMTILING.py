#입력 
# 3
# 2
# 4
# 92

#출력
# 0
# 2
# 913227494
#코드풀이 참고 https://jinu0418.tistory.com/39


import sys

input = sys.stdin.readline
mod = 1000000007


def _init_():
    global dp
    dp = [-1] * 101
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    dp[4] = 5 # 4 아님

def Tiling(n):
    global dp

    if dp[n] != -1:
        return dp[n] % mod

    dp[n] = (Tiling(n-1)%mod + Tiling(n-2)%mod) %mod #경우의 수가 음수가 나오지 않게 하기 위해서
    return dp[n]

def asymmetric(n):
    global dp
    ret = Tiling(n)

    # 비대칭 구하는 법 : 전체 수 - 대칭 수


    if ((n - 1) % 2 == 0):
        ret = (ret - Tiling((n - 1) // 2) + mod) % mod
    if ((n - 2) % 2 == 0):
        ret = (ret - Tiling((n - 2) // 2) + mod) % mod
    if (n % 2 == 0):
        ret = (ret - Tiling(n // 2) + mod) % mod

    return ret



for _ in range(int(input())):
    _init_()
    n = int(input())
    if n == 2: #dp[2] 초기화에서 문제가 있다고 해서
        print(0)
    else:
        print(asymmetric(n)) #숫자가 너무 커서 문제조건에 맞게 나머지로 output



