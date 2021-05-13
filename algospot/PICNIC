# 아직 문제 풀이중..
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

# TODO
# 입력 제작 ok
# Pair에서 2개씩 잘라서  ok
# 실제 페어를 숫자마다 정리 (pair_dict)  0 : [0,1], 1: [0,1] ok
# 맨 처음 pair를 제외한 숫자중에 [0,1] 제외 2~5 여기서 조합에서 pair_dict에 존재하는지 확인 ok
# 만약에 존재하면 남은 숫자를 가지고 재귀 수행 
# 없으면 
# 그렇게 리스트 len이 될때까지 반복 존재하는 것 다찾으면 cnt 증가
import sys
from itertools import combinations

def find(left_pair, m, pair_dict):
    for idx in range(m-1):

        # pair_dict에 this_pair가 있는지 확인 
        if left_pair in pair_dict:
            find(left_pair[2:], m, pair_dict)
        
        
    
c = int(input())
for _ in range(c):
    nm_list = list(map(int, sys.stdin.readline().split()))
    n, m = nm_list[0], nm_list[1]
    pair = list(map(int, sys.stdin.readline().split()))

    pair_dict = {}
    for idx in range(m):
        this_pair= pair[idx*2:idx*2+2]
        first, second = this_pair[0], this_pair[1]
        print(this_pair)

        if this_pair[0] in pair_dict:
            pair_dict[this_pair[0]].append(this_pair)
        else:
            pair_dict[this_pair[0]] = [this_pair]

        if this_pair[1] in pair_dict:
            pair_dict[this_pair[1]].append(this_pair)
        else:
            pair_dict[this_pair[1]] = [this_pair]

    left_pair = pair[2:]
    find(left_pair, m, pair_dict)



    print(_, pair_dict)
