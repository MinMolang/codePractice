# https://www.acmicpc.net/problem/4963
# 대각선 이동도 가능함에 유의


import sys
from functools import reduce
dx = [0,0,1,-1,-1,-1,1,1]
dy = [1,-1,0,0,1,-1,1,-1]
def bfs(i,j,cnt):
    q = []
    q.append((i,j))
    board[i][j] = cnt


    while q:
        x = q[0][0]
        y = q[0][1]
        q.pop(0)
        for k in range(8):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<m: #정사각행렬이 아니니까 ,n,m 유의할 것
                if a[nx][ny]==1 and board[nx][ny] ==0:
                    q.append((nx,ny))
                    board[nx][ny] = cnt


while True:
    m, n = map(int, sys.stdin.readline().strip().split())
    a =[]
    board = [[0]*m for _ in range(n)] #0일 경우에 0으로 대답하기 위해, -1말고 0으로 초기화
    cnt = 0
    if m==0 and n==0:
        break
    for x in range(n):
        listx = list(map(int, sys.stdin.readline().strip().split()))
        a.append(list(listx))
    #     a = [list(map(int,input().split())) for _ in range(n)] 위의 두줄을 이 한 줄로 바꿀 수 있음 ㅠㅠ, 대신 위에 a= []지울 것
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1 and board[i][j] == 0:
                cnt += 1
                bfs(i, j, cnt)
    print(cnt)
    '''        
    ㅠㅠ 굳이 이렇게 하지 않아도 print(cnt)하면 섬의 개수가 나옴 ㅠㅠ
    ans = reduce(lambda x, y: x + y, board)  # 리스트 붙이는 효과, 2차배열을 1차배열로
    print(max(ans)) 
    
    '''
