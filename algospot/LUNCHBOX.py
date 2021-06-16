# 입력
# 2
# 3
# 2 2 2
# 2 2 2
# 3
# 1 2 3
# 1 2 1
#
# 출력
# 8
# 7


# 탐욕법
# 어차피 마지막 도시락 데운 사람이 먹는 것을 기다려줘야 하니
# 마지막 도시락은 가장 빨리 먹는 사람 것을 고르자!

import sys

input = sys.stdin.readline

def heat():
    '''

    점심을 먹는데 최소 시간을 return

    :return:
        ret(str)
    '''

    # 어느 순서로 데워야 할지를 정한다.
    #order :  eating pair (- eatingtime, index)
    order = []
    for i in range(n):
        order.append((-eating[i], i))

    sorted_order = sorted(order, key=lambda x: x[0])

    # 해당 순서대로 데워 먹는 과정을 시뮬레이션한다.
    ret, beginEat = 0,0
    for i in range(n):
        box = sorted_order[i][1] # 인덱스 가져오기, 가장 빨리 먹는 도시락
        beginEat += heating[box] # 도시락 데우는 시간들 다 더하기
        ret = max(ret, beginEat + eating[box]) #ret, 모든 도시락을 데우는 시간 + 도시락 하나를 먹는 시간

    return ret

for _ in range(int(input())):
    n = int(input())
    heating = list(map(int, input().strip().split()))
    eating = list(map(int, input().strip().split()))

    print(heat())


