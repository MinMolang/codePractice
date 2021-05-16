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

# python 코드 출처 https://junho-one.tistory.com/4
import sys

def pairing( finished ) :
    # 모두 True면 끝난 상황
    # 기저사례, 모든 짝을 찾았으면 종료해준다.
    if all(finished) :
        return 1

    # False인 사람 인덱스 찾기
    # 남은 학생들 중 가장 번호가 빠른 학생을 찾는다.
    first_people = finished.index(False)
    count = 0

    # 이 첫번째 학생과 짝을 지을 학생을 찾아준다
    for i in range(first_people+1, len(finished)) :

        if not finished[i] and areFriend[first_people][i] :

            finished[i] = True
            finished[first_people] = True
            count += pairing(finished)
            finished[i] = False
            finished[first_people] = False

    return count

c = int(input())
for _ in range(c):
    nm_list = list(map(int, sys.stdin.readline().split()))
    n, m = nm_list[0], nm_list[1]
    line = list(map(int, sys.stdin.readline().split()))
    pairs = [] # 두명씩
    for i in range(0, m * 2, 2):
        pairs.append(line[i:i + 2])

    # 초기화
    areFriend = [[False for _ in range(n)] for _ in range(n)]

    # 친구판단 순서바꿔서도
    for pair in pairs:
        areFriend[pair[0]][pair[1]] = True
        areFriend[pair[1]][pair[0]] = True

    #초기화
    finished = [False for _ in range(n)]

    print(pairing(finished))



