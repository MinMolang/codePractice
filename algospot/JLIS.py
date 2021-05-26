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

# 코드 출처 : https://junho-one.tistory.com/11

import sys


def Jlis(posA, posB):  #
    # dp에 존재하는 지 확인
    if dp[posA][posB]:  # -1이 아니면 lis를 구한 것이므로 길이를 return
        return dp[posA][posB]

    ret = 2  # sequenceA[posA], sequenceB[posB]가 항상 존재하므로 2개는 항사 있다

    currA, currB = sequenceA[posA], sequenceB[posB]

    # A, B 둘 중에 큰 숫자 찾기
    maxElement = max(currA, currB)

    # 다음 원소 찾기
    for nextA in range(posA + 1, lis_lenA):
        if maxElement < sequenceA[nextA]:
            ret = max(ret, Jlis(nextA, posB) + 1)

    for nextB in range(posB + 1, lis_lenB):
        if maxElement < sequenceB[nextB]:
            ret = max(ret, Jlis(posA, nextB) + 1)

    dp[posA][posB] = ret  # dp에 저장 후 리턴
    return ret


c = int(input())
for i in range(c):
    lis_len = list(map(int, sys.stdin.readline().strip().split()))
    lis_lenA, lis_lenB = lis_len[0], lis_len[1]
    sequenceA = list(map(int, sys.stdin.readline().rstrip().split()))
    sequenceB = list(map(int, sys.stdin.readline().rstrip().split()))

    # 음수정수값 추가
    # 함수 자체가 다음값을 구해나가는 과정이 있어서
    sequenceA.insert(0, -sys.maxsize + 1)
    sequenceB.insert(0, -sys.maxsize + 1)

    # 음수정수값 추가한만큼 길이 추가
    lis_lenA += 1
    lis_lenB += 1

    # 다이나믹 프로그래밍 메모이제이션
    dp = [[None for _ in range(lis_lenB)] for _ in range(lis_lenA)]

    # 더해준 2개 다시 빼주기
    print(Jlis(0, 0) - 2)