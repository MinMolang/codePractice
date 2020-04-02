'''
<2차원 리스트 만들기>

board = [[0]*m for _ in range(n)] #0으로 초기화
a = [list(map(int,input().split())) for _ in range(n)] #2차 행렬 읽어들이기

'''

'''
<상하좌우, 대각선 이동 (앞의 4개가 상하좌우)>

dx = [0,0,1,-1,-1,-1,1,1]
dy = [1,-1,0,0,1,-1,1,-1]

for k in range(8):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0<=nx<n and 0<=ny<m: #정사각행렬이 아니니까 ,n,m 유의할 것
            if a[nx][ny]==1 and board[nx][ny] ==0:
                q.append((nx,ny))
'''

'''
<2차원 1차원으로 줄이기 및 기타>

from collections import Counter
from functools import reduce

ans = reduce(lambda x,y:x+y,house) # 리스트 붙이는 효과, 2차배열을 1차배열로
ans = [x for x in ans if x>0] # 1이상인 애들만 가져오기

ans = sorted(list(Counter(ans).values())) #1 개수 : 7, 2개수 8, 3 개수 9 [7,8,9] 만든 뒤에 오름차순 배열
print(cnt) #총단지수
print('\n'.join(map(str,ans))) #리스트 string으로 만들고 줄바꿈 추가

'''


'''
<bfs 구현체 , 단 cnt 추가 >

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

'''
'''
<덱 사용하기>

list 앞에 추가하려면 deque이 속도가 더 빠르다 

from collections import deque
def bfs(x, y, cnt):
    q = deque()  #덱만들기
    q.append((x,y)) #덱오른쪽에 추가 
    group[x][y] = cnt
    while q:
        x, y = q.popleft() #덱왼쪽에서 빼내기 
    d.pop() #덱 오른쪽에서 빼내기
    d.appendleft(0) #덱왼쪽으로 추가 
    
'''