# 입력
# 3
# 2 1
# 0 1
# 4 6
# 0 1 1 2 2 3 3 0 0 2 1 3
# 6 10
# 0 1 0 2 1 2 1 3 1 4 2 3 2 4 3 4 3 5 4 5

# 출력
# 1
# 3
# 4

# 4 예시 )
# 0 1 / 2 3/ 4 5
# 0 1 / 2 4 / 3 5
# 0 2 / 1 3 / 4 5
# 0 2 / 1 4 / 3 5

#풀이
# 짝을짓고, 남은 학생들에 대해서 다시 짝을 지어주는 재귀함수
# 중복을 방지하기 위해 특정한 형태만 세준다 (sort) 0, 1은 세주고 ,1, 0 은 세주지 않는다
# 0,1 2,3과 2,3 0,1은 같은 것인 문제도 sort해서 특정한 형태로 세주게 되면 문제 해결
import sys
from itertools import combinations

n = 0
areFriends = []

# taken[i] i번째 학생이 짝을 이미 찾았으면 True, 아니면 FALSE
def countPairings(taken):
    # 남은 학생들 중 가장 번호가 빠른 학생을 찾는다.
    firstFree = -1
    for i in range(n):
        if not taken[i]:
            firstFree = i
            break

    # 기저사례, 모든 짝을 찾았으면 종료해준다.
    if firstFree == -1 :
        return 1

    ret = 0
    # 이 학생과 짝을 지을 학생을 찾아준다
    for pairWith in range(firstFree+1, n):
        if not taken[pairWith] and areFriends[firstFree][pairWith]:
            taken[firstFree] = taken[pairWith] = True
            ret += countPairings(taken)
            taken[firstFree] = taken[pairWith] = False
    return ret


c = int(input())
for _ in range(c):
    nm_list = list(map(int, sys.stdin.readline().split()))
    n, m = nm_list[0], nm_list[1]
    pair = list(map(int, sys.stdin.readline().split()))

    ret = countPairings(pair)
    print(ret)


