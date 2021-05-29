# 입력
# 5
# 12341234
# 11111222
# 12122222
# 22222222
# 12673939

# 출력
# 4
# 2
# 5
# 2
# 14

# 모든 숫자가 같을 때 (예: 333, 5555) 난이도: 1
# 숫자가 1씩 단조 증가하거나 단조 감소할 때 (예: 23456, 3210) 난이도: 2
# 두 개의 숫자가 번갈아 가며 출현할 때 (예: 323, 54545) 난이도: 4
# 숫자가 등차 수열을 이룰 때 (예: 147, 8642) 난이도: 5
# 그 외의 경우 난이도: 10

# 풀이 출처 : doctidea님 풀이
import  sys

sys.setrecursionlimit(10**6)

# numbers [a,b,c] 세자리 구간의 난이도를 반환
def score_3(a, b, c):
    # 숫자 조각을 가져온다
    if a == b == c: # 모든 숫자 같음
        return 1
    if a-b == b-c == 1 or a-b == b-c == -1: #단조증가/감소
        return 2
    if a==c!=b: # 숫자가 번갈아가면서 출현
        return 4
    if a-b == b-c: # 등차수열
        return 5
    return  10

# numbers [a,b,c,d] 네자리 구간의 난이도를 반환
def score_4(a, b, c, d):
    # 숫자 조각을 가져온다
    if a == b == c == d: # 모든 숫자 같음
        return 1
    if a-b == b-c == c-d  == 1 or a-b == b-c == c-d ==  -1: #단조증가/감소
        return 2
    if a == c and b == d and a!=b: # 숫자가 번갈아가면서 출현
        return 4
    if a-b == b-c == c-d: # 등차수열
        return 5
    return  10

# numbers [a,b,c,d,e] 다섯자리 구간의 난이도를 반환
def score_5(a, b, c, d,e):
    # 숫자 조각을 가져온다
    if a == b == c == d == e: # 모든 숫자 같음
        return 1
    if a-b == b-c == c-d == d-e == 1 or a-b == b-c == c-d == d-e ==  -1: #단조증가/감소
        return 2
    if a == c == e and b == d and a != b: # 숫자가 번갈아가면서 출현
        return 4
    if a-b == b-c == c-d == d-e: # 등차수열
        return 5
    return  10


def memorize(numbers):
    N = len(numbers)
    dp = [None]*(N+1)
    dp[3] = score_3(numbers[0], numbers[1], numbers[2]) # 3개까지 읽음
    dp[4] = score_4(numbers[0], numbers[1], numbers[2], numbers[3]) # 4개까지 읽음
    dp[5] = score_5(numbers[0], numbers[1], numbers[2], numbers[3], numbers[4]) #5개까지 읽음
    for i in range(6, N+1):
        cand = []
        if dp[i-3] is not None:
            cand.append(dp[i-3] + score_3(numbers[i-3], numbers[i-2], numbers[i-1]))
        if dp[i-4] is not None:
            cand.append(dp[i-4] + score_4(numbers[i-4], numbers[i-3], numbers[i-2], numbers[i-1]))
        if dp[i-5] is not None:
            cand.append(dp[i-5] + score_5(numbers[i-5], numbers[i-4], numbers[i-3], numbers[i-2], numbers[i-1]))

        dp[i] = min(cand) # 최소값을 다시 메모이제이션
    return dp[-1] #마지막 값을 제공





for _ in range(int(input())):
    numbers = list(map(int, list(input().strip())))
    dp = [-1] * len(numbers)
    print(memorize(numbers))




