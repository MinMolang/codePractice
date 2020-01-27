# https://www.acmicpc.net/problem/2206
# 벽 부수고 이동하기
# 벽부수는것.. 3차배열..

import sys
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n, m= list(map(int, sys.stdin.readline().split()))
a = [list(map(int,list(input()))) for _ in range(n)]
visit = [[[0]*2 for y in range(m)] for x in range(n)]  #[0][0] 벽을 뚫었거나, 안뚫었거나
q = deque()
q.append((0,0,0))
visit[0][0][0] = 1 #처음 시작할때

while q:
    x, y ,z = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m: #n*n이 아니라 n*m임에 유의하자
            if a[nx][ny] == 0 and visit[nx][ny][z] == 0:# 0이어서 지나갈 수 있는 곳 and  아직 방문한 적이 없는 곳이면
                visit[nx][ny][z] = visit[x][y][z]+1 # 현재까지의 이동거리 +1
                q.append((nx, ny, z))
            if z == 0 and a[nx][ny] == 1 and visit[nx][ny][z+1] == 0:# 아직 벽을 부수지 않았고 and 다음 탐색 위치의 벽이 있고 and 다음 탐색+벽을 부술위치가 방문하지 않았다면
                visit[nx][ny][z+1] = visit[x][y][z] + 1 # 현재위치가 z+1이 아니고 z여야한다.  벽을 부술 다음 위치 : 현재까지의 이동거리+1
                q.append((nx, ny, z+1))


if visit[n-1][m-1][0]!=0 and visit[n-1][m-1][1]!= 0: #끝까지 방문했다면 (마지막 위치 벽을 부수지 않은경우, 벽을 부순경우 모두)
    print(min(visit[n-1][m-1])) #마지막위치에서 벽을 부순경우와, 부수지 않은 경우 둘 중 최솟값을 선택
elif visit[n-1][m-1][0] != 0: #마지막 위치에서 벽을 부수지 않고 도달 and 마지막 위치 벽을 부순 경우는 체크
    print(visit[n-1][m-1][0])
elif visit[n-1][m-1][1] != 0: #마지막 위치에서 벽을 부수고 도달 and 마지막 위치 벽을 안부순 경우는 체크
    print(visit[n-1][m-1][1])
else: #불가능한경우
    print(-1)