import sys

#1. for문 3번 돌면서 벽을 세울 위치를 선정
#2. BFS 탐색

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(i, j):
    q = []
    q.append((i, j))
    while q:
        x = q[0][0]
        y = q[0][1]
        q.pop(0)
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if a[nx][ny]==0 and visit[nx][ny] ==0:
                    q.append((nx,ny))
                    visit[nx][ny] = 2

n, m= list(map(int, sys.stdin.readline().split()))
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
            if a[i][j] == 0 and visit[i][j] == 0:
                bfs(i,j)
#3. for문 한번 돌면서 안전영역을 찾는다.
cnt = 0
for i in range(n):
    for j in range(m):
        if visit[i][j] == 0:
            cnt+=1

print(cnt)
