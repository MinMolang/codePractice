#입력 
#3
#1
#5
#100

#출력
#1
#8
#782204094
#코드풀이 참고 https://programming119.tistory.com/113

import sys

input = sys.stdin.readline

dp = [-1 ] * 101
def Tiling2(n):
    if dp[n] != -1:
        return dp[n]
    # 없으면 Out of Index
    if n <= 0:
        return false
    if n==1:
        return 1
    if n==2:
        return 2
    dp[n] = Tiling2(n-1) + Tiling2(n-2) 
    return dp[n]
for _ in range(int(input())):
    print(Tiling2(int(input()))  % 1000000007) #숫자가 너무 커서 문제조건에 맞게 나머지로 output

