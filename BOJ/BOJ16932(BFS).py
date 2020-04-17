# https://www.acmicpc.net/problem/16932
# 모양 만들기
# BFS 탐색

import sys
from collections import Counter,deque
from functools import reduce

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(i,j):
    global groupn
    groupn+=1
    q = deque()
    q.append((i,j))
    shape[i][j] = groupn #그룹소속
    cnt =1
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if a[nx][ny]==1 and shape[nx][ny] ==0:
                    q.append((nx,ny))
                    shape[nx][ny] = groupn
                    cnt+=1
    group.append(cnt) #그룹소속에 따른 개수 (q.탐색이 끝나면 저장하기)

n, m= list(map(int, sys.stdin.readline().split()))
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
shape = [[0]*m for _ in range(n)]
groupn = 0
group = [0] #모양에 따른 그룹 사이즈

for i in range(n):
    for j in range(m):
        if a[i][j] ==1 and shape[i][j]==0:
              bfs(i,j)

ans = 0
for i in range(n):
    for j in range(m):
        near = set() #왼쪽 위쪽 같은 3번의 그룹일 경우 한번만 저장하기 위해서 , 그룹당 1번
        for k in range(4):
            nx,ny = i+dx[k],j+dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 1:
                    near.add(shape[nx][ny]) # 인접그룹을 넣는다
        s = 1
        for neighbor in near:
            s += group[neighbor] #인접 모양이랑 합치기
        if ans<s:
            ans = s #최대 길이 업데이트
print(ans)
