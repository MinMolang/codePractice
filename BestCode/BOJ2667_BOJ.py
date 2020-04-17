# https://www.acmicpc.net/problem/2667
# 단지번호 붙이기
# 80ms(+deque 활용)
from collections import deque, Counter
from functools import reduce
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(x, y, cnt):
    q = deque()
    q.append((x,y))
    group[x][y] = cnt
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] == 1 and group[nx][ny] == 0:
                    q.append((nx,ny))
                    group[nx][ny] = cnt
n = int(input())
a = [list(map(int,list(input()))) for _ in range(n)]
group = [[0]*n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and group[i][j] == 0:
            cnt += 1
            bfs(i, j, cnt)

ans = reduce(lambda x,y:x+y,house) # 리스트 붙이는 효과, 2차배열을 1차배열로
ans = [x for x in ans if x>0] # 1이상인 애들만 가져오기

ans = sorted(list(Counter(ans).values())) #1 개수 : 7, 2개수 8, 3 개수 9 [7,8,9] 만든 뒤에 오름차순 배열
print(cnt) #총단지수
print('\n'.join(map(str,ans))) #리스트 string으로 만들고 줄바꿈 추가
