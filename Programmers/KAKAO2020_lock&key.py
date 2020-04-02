# https://programmers.co.kr/learn/courses/30/lessons/60059
# 자물쇠와 열쇠

# 오전11:01 시작 미완성
import numpy as np
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
dx = [0,0,0,1,-1]
dy = [0,1,-1,0,0]
a = np.array(key)
at = np.transpose(a)
bkey = at[:, ::-1]
bt = np.transpose(bkey)
ckey= bt[:, ::-1]
ct = np.transpose(ckey)
dkey = ct[:, ::-1]
def check(nx,ny):
    # 1. 0도 회전
    # 체크해야되는 lock의 범위는 vlock에서
    #  n(klen-1)+llen 만 검사하면 됨
    klen = len(key)
    llen = len(lock)
    ans = 1
    m = llen + 2 * klen - 2
    jlock = [[0] * m for _ in range(m)]

    for x in range(klen):
        print(key[x])
        for y in range(klen):
            jlock[nx+x][ny+y] = key[x][y]


    for i in range(llen):
        print(lock[i]," ",jlock[klen-1+i])
        for j in range(llen):
            sx ,sy = klen-1+i,klen-1+j
            it = lock[i][j] ^jlock[sx][sy]
            # print("i,j,it",i,j,it)
            ans = ans*it
            # 만약 nx ~ nx+klen key의 범위만큼
            # print(lock[i][j] ,key[i][j],lock[i][j]^key[i][j])

            # sx,sy = klen -1,klen-1 #startpoint
            # if sx<nx+klen and sy<ny+klen:
            #     # print("i ama okay ",sx,sy)
            #     pass
            # else:
            #     # print("i ama not okay",sx,sy)
            #     pass
            jlock[sx][sy] = it
    print(nx,ny,"0")
    for k in jlock:
        print(k)
    if ans == 1:
        return True
    else:
        return False


def check2(nx, ny):
    # 2. 90도 회전
    klen = len(key)
    llen = len(lock)
    ans = 1
    m = llen + 2 * klen - 2
    jlock = [[0] * m for _ in range(m)]



    for x in range(klen):
        for y in range(klen):
            jlock[nx + x][ny + y] = bkey[x][y]

    for i in range(llen):
        for j in range(llen):
            sx, sy = klen - 1 + i, klen - 1 + j
            it = lock[i][j] ^ jlock[sx][sy]
            ans = ans * it
            jlock[sx][sy] = it
    print(nx,ny,"90")
    for k in jlock:
        print(k)
    if ans == 1:
        return True
    else:
        return False

def check3(nx, ny):
    # 3. 180도 회전
    klen = len(key)
    llen = len(lock)
    ans = 1
    m = llen + 2 * klen - 2
    jlock = [[0] * m for _ in range(m)]

    for x in range(klen):
        for y in range(klen):
            jlock[nx + x][ny + y] = ckey[x][y]


    for i in range(llen):
        for j in range(llen):
            sx, sy = klen - 1 + i, klen - 1 + j
            it = lock[i][j] ^ jlock[sx][sy]
            ans = ans * it
            jlock[sx][sy] = it
    print(nx,ny,"180")
    for k in jlock:
        print(k)
    if ans == 1:
        return True
    else:
        return False


def check4(nx, ny):
    # 4. 270도 회전
    klen = len(key)
    llen = len(lock)
    ans = 1
    m = llen + 2 * klen - 2
    jlock = [[0] * m for _ in range(m)]

    for x in range(klen):
        for y in range(klen):
            jlock[nx + x][ny + y] = dkey[x][y]

    for i in range(llen):
        for j in range(llen):
            sx, sy = klen - 1 + i, klen - 1 + j
            it = lock[i][j] ^ jlock[sx][sy]
            ans = ans * it
            jlock[sx][sy] = it
    print(nx,ny,"270")
    for k in jlock:
        print(k)
    if ans == 1:
        return True
    else:
        return False
def solution(key, lock):
    # 1. 가상이 lock 환경 a 2차 행렬 만들기
    klen = len(key)
    llen = len(lock)
    m = llen + 2*klen -2
    n = klen-1
    vlock = [[-1] * m for _ in range(m)]
    print(vlock)
    # a = [[0] * m for _ in range(n)]
    # for _ in range(llen):
    #     x = [0]*n
    #     x +=lock[_]
    #     x +=[0]*n
    #     a.append(x)
    # a.append([[0] * m for _ in range(n)])
    # 2. 탐색해야할 영역 이동 부분 완성
    q = []
    q.append((n, n)) #klen -1 부터 시작 (lock의 원래 위치
    print("q",q)
    # vlock[n][n] = 0
    ans = False
    while q:
        x = q[0][0]
        y = q[0][1]
        # 이동하여탐색
        q.pop(0)
        for k in range(5):
            nx = x + dx[k]
            ny = y + dy[k]
            print("nx,ny", nx,ny)
            if 0 <= nx <m-n and 0 <= ny < m-n: #범위는 m(vlock 전체 크기) 에서 n(klen-1) 만큼 빼준 55
                if vlock[nx][ny] == -1:
                    if (check(nx,ny) or check2(nx,ny)or check3(nx,ny)or check4(nx,ny)) == True:
                        # ans = True
                        # break
                        return True
                    vlock[nx][ny] = 0
                    q.append((nx, ny))

    print(vlock)
    return ans

    # 2. a 전체를 key의 범위만큼 모두 탐색
    # 실질적 lock이 존재하는 범위만 비교해서 모두 xor이 되면 되는데
    # each 파트마다 비교해야하나?







    '''열쇠의 돌기가 자물쇠의 홈과 맞는기 찾기'''
    # ([(1, 2), (2, 1)],lock [(1, 0), (2, 1), (2, 2)]) key


    #어떻게 맞출지 한번 생각해보기
    #일단, 한꺼번에 영역을 모아야하는 걸까? 그 다음에 이동, 회전을 시키고
    # 안되게 되면 STOP하고, 되면 TRUE로 내고?
    # 3BY3 , 2 BY 2 이런 것 알 필요 있을까? 없을 듯, 돌기끼리 겹치지만 않으면 되니까?
    # 각 회전에서 이동까지 검사
    # 0. 0도 회전
    # 1. 90도 회전
    # 2. 180도 회전
    # 3. 270도 회전
    # 키를 회전 이동 여러번 한다음에 1) 자물쇠의 모든 홈이 채워지고 2) 돌기가 겹치지 않는다면 탐색 종료



print(solution(key,lock))

'''
a = [[1,2,3],[4,5,6],[7,8,9]]
a = np.array(a)
at = np.transpose(a)
b = at[:, ::-1]
print('90',b)
bt = np.transpose(b)
c = bt[:, ::-1]
print('180',c)
ct = np.transpose(c)
d = ct[:, ::-1]
print('270',d)

#자물쇠의 홈 영역 좌표로 만들기 
lpos = []
kpos = []
for x, row in enumerate(lock):
    for y, col in enumerate(row):
        if col == 0:
            lpos.append((x, y))

# 열쇠의 돌기 영역 좌표로 만들기 
for x, row in enumerate(key):
    for y, col in enumerate(row):
        if col == 1:
            kpos.append((x, y))
'''

