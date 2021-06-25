# 입력
# 5
# 10 8
# 100 80
# 47 47
# 99000 0
# 1000000000 470000000

#출력
# 1
# 6
# -1
# 1000
# 19230770

# 일단 현재의 승률을 구하자

import sys

MAX_NUM = 2000000000

def ratio(games, won):
    return won * 100 // games #꼭 //로 나눠주기

def neededGames(games, won):

    # 2, 000, 000, 000 연승해도 승률이 오를 수 없는 경우
    if ratio(games, won) == ratio (games + MAX_NUM, won + MAX_NUM):
        return -1

    lo, hi = 0 , MAX_NUM

    # 반복문 불변식
    # 1. lo게임 이기면 승률은 변하지 않는다.
    # 2. hi게임 이기면 승률은 변한다.

    while(lo + 1 < hi):
        mid = (lo + hi) // 2 # 꼭 //2로 나눠주기
        if ratio(games, won) == ratio(games + mid, won + mid):
            lo = mid
        else:
            hi = mid

    return hi

for _ in range(int(input())):
    n, m = map(int, sys.stdin.readline().strip().split())
    print(neededGames(n, m))

    # 상수 시간 방정식 답구하기 테스트
    # z =  m * 100 // n
    # ans =  (z+1) * n - 100 * m // ( 100 - (z+1) )
    # ans = math.ceil(ans)
    # print(ans)