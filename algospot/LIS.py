# 입력
# 3
# 4
# 1 2 3 4
# 8
# 5 4 3 2 1 6 7 8
# 8
# 5 6 7 8 1 2 3 4

# 출력
# 4
# 4
# 4

# 코드 출처 : https://doctcoder.tistory.com/28

import sys

def lis(pos): #
    # dp에 존재하는 지 확인
    if dp[pos] != -1: # -1이 아니면 lis를 구한 것이므로 길이를 return
        return dp[pos]


    ret = 1 # 항상 start는 있기 때문에 길이 최하는 1
    for i in range(pos, lis_len):
        if sequence[pos] < sequence[i]:
            ret = max(ret, lis(i) + 1) # 자신을 포함하기 때문에 1을 더해줌

    dp[pos] = ret #dp에 저장 후 리턴
    return ret


c = int(input())
for i in range(c):
    lis_len = int(input())
    sequence = list(map(int, sys.stdin.readline().rstrip().split()))
    dp = [-1 for j in range(lis_len)] # 메모이제이션 , lis 길이를 저장
    ans = 0
    for k in range(lis_len):
        ans = max(ans, lis(k)) # sequence의 0번째부터 lis 길이 탐색
    print(ans)