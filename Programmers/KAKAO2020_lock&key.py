# https://programmers.co.kr/learn/courses/30/lessons/60059
# 자물쇠와 열쇠
import numpy as np
dx = [0,0,0,1,-1]
dy = [0,1,-1,0,0]

def check(nx,ny,key,lock):
    # 1. 0도 회전
    klen = len(key)
    llen = len(lock)
    ans = 1
    m = llen + 2 * klen - 2
    jlock = [[0] * m for _ in range(m)]

    for x in range(klen):
        for y in range(klen):
            jlock[nx+x][ny+y] = key[x][y]


    for i in range(llen):
        for j in range(llen):
            sx ,sy = klen-1+i,klen-1+j
            it = lock[i][j] ^jlock[sx][sy]
            ans = ans*it
            jlock[sx][sy] = it

    if ans == 1:
        return True
    else:
        return False


def check2(nx, ny,bkey,lock):
    # 2. 90도 회전
    klen = len(bkey)
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

    if ans == 1:
        return True
    else:
        return False

def check3(nx, ny,ckey,lock):
    # 3. 180도 회전
    klen = len(ckey)
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

    if ans == 1:
        return True
    else:
        return False


def check4(nx, ny,dkey,lock):
    # 4. 270도 회전
    klen = len(dkey)
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

    if ans == 1:
        return True
    else:
        return False
def solution(key, lock):
    a = np.array(key)
    at = np.transpose(a)
    bkey = at[:, ::-1]
    bt = np.transpose(bkey)
    ckey= bt[:, ::-1]
    ct = np.transpose(ckey)
    dkey = ct[:, ::-1]
    # 1. 가상이 lock 환경 a 2차 행렬 만들기
    klen = len(key)
    llen = len(lock)
    m = llen + 2*klen -2
    n = klen-1
    vlock = [[-1] * m for _ in range(m)]
    q = []
    q.append((n, n))
    ans = False
    while q:
        x = q[0][0]
        y = q[0][1]
        # 이동하여탐색
        q.pop(0)
        for k in range(5):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx <m-n and 0 <= ny < m-n: #범위는 m(vlock 전체 크기) 에서 n(klen-1) 만큼 빼준
                if vlock[nx][ny] == -1:
                    if (check(nx,ny,key,lock) or check2(nx,ny,bkey,lock)or check3(nx,ny,ckey,lock)or check4(nx,ny,dkey,lock)) == True:
                        return True
                    vlock[nx][ny] = 0
                    q.append((nx, ny))

    return ans