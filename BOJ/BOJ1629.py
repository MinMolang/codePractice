# https://www.acmicpc.net/problem/1629
# 곱셈
# divide and conquer
#56ms

import sys
def DC(a,b,c):
    # 종료조건
    print(b)
    if b == 0:
        return 1
    if b%2 ==1 :# 홀수번 곱했을 때,

        return DC(a, b-1,c)*a%c
    else:# 짝수번 곱햇을 떄,
        it = DC(a,b/2,c)%c
        print(b, it*it%c)
        return it*it%c

    return ans
a,b,c = list(map(int, sys.stdin.readline().strip().split()))
print(DC(a,b,c))

# 호출순서
# b = 11
# b = 10
# b = 5
# b = 4
# b = 2
# b = 1
# b = 0
#
# (b|0) = 1
# (b|1) = 1*10%12 =10
# (b|2) = (10%12)*(10%12)%12 = 4
# (b|4) = (4%12)*(4%12)%12 = 4
# (b|5) = 4*10%12 = 4
# (b|10) = (4%12)*(4%12)%12 = 4
# (b|11) = 4*10%12 = 4

