# https://www.acmicpc.net/problem/2667
# 단지번호 붙이기
# 88ms Best code는 80ms(+deque 활용)
import sys
from collections import Counter
from functools import reduce
def bfs(i,j,cnt):
    q = []
    q.append((i,j))
    house[i][j] = cnt
    while q:
        x = q[0][0]
        y = q[0][1]
        q.pop(0)
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<n:
                if a[nx][ny]==1 and house[nx][ny] ==0:
                    q.append((nx,ny))
                    house[nx][ny] = cnt
n = int(sys.stdin.readline())
a = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for x in range(n):
    listx = list(map(int,sys.stdin.readline().strip()))
    a.append(list(listx))

cnt = 0
house = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if a[i][j] ==1 and house[i][j]==0:
            cnt+=1
            bfs(i,j,cnt)

ans = reduce(lambda x,y:x+y,house) # 리스트 붙이는 효과, 2차배열을 1차배열로
ans = [x for x in ans if x>0] # 1이상인 애들만 가져오기

ans = sorted(list(Counter(ans).values())) #1 개수 : 7, 2개수 8, 3 개수 9 [7,8,9] 만든 뒤에 오름차순 배열
print(cnt) #총단지수
print('\n'.join(map(str,ans))) #리스트 string으로 만들고 줄바꿈 추가
