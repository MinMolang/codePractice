import sys

'''

출력

3
3


3 3
0 7

3 3
1 0 

1
1

'''

import sys
from collections import Counter
from functools import reduce
def bfs(i,j,cnt):
    q = []
    q.append((i,j))
    visit[i][j] = cnt
    while q:
        x = q[0][0]
        y = q[0][1]
        q.pop(0)
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if visit[nx][ny] ==-1:
                    q.append((nx,ny))
                    visit[nx][ny] = visit[x][y] +cnt
dx = [0,0,1,-1]
dy = [1,-1,0,0]

n, m = list(map(int, sys.stdin.readline().strip().split()))
cnt = 0
visit = [[-1]* m for _ in range(n)]
ax, ay = list(map(int, sys.stdin.readline().strip().split()))
if (ax == 0 or ax>=n) and (ay == 0 or ay>= m):
    print("fail")
else:

    for i in range(n):
        for j in range(m):
            if visit[i][j]==-1:
                print("hi")
                cnt += 1
                bfs(i,j,cnt)


    print(visit)
    ans = visit[ax][ay]-1
    it = reduce(lambda x,y:x+y,visit)
    itcnt = Counter(it)
    ans2 = itcnt[ans]
    print(ans)
    print(ans2)
#
# ans = reduce(lambda x,y:x+y,visit) # 리스트 붙이는 효과, 2차배열을 1차배열로
#
# ans = [x for x in ans if x>0] # 1이상인 애들만 가져오기
#
# ans = sorted(list(Counter(ans).values())) #1 개수 : 7, 2개수 8, 3 개수 9 [7,8,9] 만든 뒤에 오름차순 배열
# print(cnt) #총단지수
# print('\n'.join(map(str,ans))) #리스트 string으로 만들고 줄바꿈 추가
#
# # q = []
# # q.append((fx, fy))
# # board[fx][fy] = 0
# # while q:
# #     x = q[0][0]
# #     y = q[0][1]
# #     q.pop(0)
# #     for k in range(8):
# #         nx = x + dx[k]
# #         ny = y + dy[k]
# #         if 0 <= nx < sqr and 0 <= ny < sqr:
# #             if board[nx][ny] == -1:
# #                 board[nx][ny] = board[x][y] + 1
# #                 q.append((nx, ny))