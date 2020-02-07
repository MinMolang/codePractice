# https://www.acmicpc.net/problem/1260
# BFS/DFS
#76ms..!
import sys
input = sys.stdin.readline()
v,e,s = map(int,input.split()) #vertex 개수, edge 개수, 시작점
# 1. 그래프만들기
edge = [[] for x in range(v+1)] #그래프 시작은 0 이 아니라 1부터

for j in range(e):
    sent = sys.stdin.readline()
    a,b = map(int,sent.split())
    edge[a].append(b)
    edge[b].append(a)

#2. 재귀로 dfs
check = [False for x in range(v+1)]
answer = []
def dfs(x):
    check[x] = True # visit
    answer.append(str(x))
    edge[x] = sorted(edge[x]) #이부분을 해줘야지 2.TEST-CASE 성공 (작은 수의 정점 먼저 방문)
    for i in range(len(edge[x])):
        next = edge[x][i]
        if check[next]==False:
            # 아직 방문하지 않았으면
            dfs(next)
dfs(s)
print(" ".join(answer))
# 3. queue역할하는 리스트로 bfs
q = [] # queue
# 초기화
check = [False for x in range(v+1)]
answer = []
check[s] = True
q.append(s)
while q:
    x = q[0]
    answer.append(str(x))
    q.pop(0)
    for i in range(len(edge[x])):
        y = edge[x][i]
        if check[y] == False:
            check[y]=True
            q.append(y)
print(" ".join(answer))




