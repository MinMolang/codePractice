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
import  sys

sys.setrecursionlimit(10**6)
INF = 987654321

# numbers [a .. b] 구간의 난이도를 반환
def classify(a, b):
    # 숫자 조각을 가져온다
    sub = numbers[a, b+1]
    # 첫 글자만으로 이루어진 문자열과 같으면 난이도 1
    if len(set(sub)) == 1:
        return  1

    progressive = True
    for i in range(len(sub) - 1):
        if (sub[i+1] - sub[i]) != (sub[1] - sub[0]):
            progressive = False
            break

    # 단조증가, 감소, = 등차수열이고 공차가 1 또는 -1이면 난이도 2
    if progressive and abs(sub[1] - sub[0]) == 1:
        return 2

    # 두 수가 번갈아 등장하는지 확인
    alternating = True
    for i in range(len(sub)):
        if sub[i] != sub[i % 2]: # 리스트 괄호 오타
            alternating  = False
            break #추가

    if alternating:
        return 4
    if progressive:
        return 5

    return 10


# 시작하는 인덱스
def memorize(begin):

    # 기저사례 : 수열의 끝에 도달했을 경우
    if begin == len(numbers):
        return 0

    # 메모이제이션
    ret = dp[begin]
    if ret != -1: # -1 초기값인지, 이미 구했는지 확인
        return ret

    ret = INF
    # 세자리수, 다섯자리 수 판단
    for num in [3, 4, 5]:
        if begin + num <= len(numbers):
            ret = min (ret, memorize(begin + num) + classify(begin, begin + num - 1)) # 구하지 않은 값이미면 최소값 구하기

    return ret

for _ in range(int(input())):
    numbers = list(map(int, list(input().strip())))
    dp = [-1] * len(numbers)
    print(memorize(0))




