# https://programmers.co.kr/learn/courses/30/lessons/60059
# 자물쇠와 열쇠

# 오전11:01 시작 미완성

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def solution(key, lock):
    # answer = True
    # return answer
    '''자물쇠의 홈 영역 좌표로 만들기 '''
    lpos = []
    kpos = []
    for x,row in enumerate(lock):
        for y,col in enumerate(row):
            if col == 0:
                lpos.append((x,y))

    '''열쇠의 돌기 영역 좌표로 만들기 '''
    for x, row in enumerate(key):
        for y, col in enumerate(row):
            if col == 1:
                kpos.append((x, y))

    '''열쇠의 돌기가 자물쇠의 홈과 맞는기 찾기'''
    #어떻게 맞출지 한번 생각해보기
    #일단, 한꺼번에 영역을 모아야하는 걸까? 그 다음에 이동, 회전을 시키고
    # 안되게 되면 STOP하고, 되면 TRUE로 내고?
    # 3BY3 , 2 BY 2 이런 것 알 필요 있을까? 없을 듯, 돌기끼리 겹치지만 않으면 되니까?
    return lpos, kpos







print(solution(key,lock))