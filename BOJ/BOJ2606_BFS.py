# https://www.acmicpc.net/problem/2606
# 바이러스
# bfs 탐색으로
# O(1과 연결되어있는 간선의 개수만큼)
# 132ms (PyPy3)
import sys

n = int(sys.stdin.readline().strip()) #노드의 개수
m = int(sys.stdin.readline().strip()) #엣지의 개수

edge = [[] for x in range(n+1)] #그래프 시작은 0 이 아니라 1부터

for j in range(m):
    sent = sys.stdin.readline()
    a,b = map(int,sent.split())
    edge[a].append(b)
    edge[b].append(a)


q = [] # queue
# 초기화
check = [False for x in range(n+1)] #방문체크역할
answer = 0
check[1] = True
q.append(1)
while q:
    x = q[0] #next 방문
    q.pop(0)
    for i in range(len(edge[x])):
        y = edge[x][i]
        if check[y] == False:#방문하지 않았다면
            check[y]=True
            q.append(y)
            answer+=1 #함수내에서가 아니라서 global 선언안해도됨
print(answer)
