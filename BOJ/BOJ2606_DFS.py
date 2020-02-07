# https://www.acmicpc.net/problem/2606
# 바이러스
# dfs 탐색으로
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


# dfs로 탐색
check = [False for x in range(n+1)] #방문했는 지 체크
answer = [0]
answer2 = 0
def dfs(x):
    check[x] = True # visit
    for i in range(len(edge[x])):
        next = edge[x][i]
        if check[next]==False:
            # 아직 방문하지 않았으면
            answer[0]+=1 #이곳에 위치한 이유는 1은 포함시키지 않으려고  포함시키려면 if 문 위에
            global answer2
            answer2 +=1
            dfs(next)
dfs(1)
print(answer2)