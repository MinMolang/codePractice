# https://www.acmicpc.net/problem/2606
# 바이러스
# Union Find로
# 140ms (PyPy3)
# 시간복잡도 O(ackerman inverse function(n))
'''
시작은 1이고
계속 부모를 찾아나가는과정이고
1과 연결되어있는 set의 개수에서 1만 뺴면 되는 건데

Union의 역할 (x,y)를 합집합시키는 것
Find의 역할 x의 부모를 찾는 역할

'''
import sys

n = int(sys.stdin.readline().strip()) #노드의 개수
m = int(sys.stdin.readline().strip()) #엣지의 개수

edge = [[] for x in range(n+1)] #그래프 시작은 0 이 아니라 1부터
parent = [x for x in range(n+1)]

rank = [0]*(n+1) #높이 비교

def Find(x):
    if x == parent[x]:
        rank[x] = 1
        return x
    else:
        y = Find(parent[x])
        parent[x] = y
        rank[x]+=1
        return y

def Union(x,y):
    x = Find(x)
    y = Find(y)
    if x == y:
        return
    if rank[x]==rank[y]:
        rank[x] = rank[y]+1
    if rank[x]>rank[y]:
        parent[y] = x
    else:
        parent[x] = y

for j in range(m):
    sent = sys.stdin.readline()
    a,b = map(int,sent.split())
    Union(a,b)

answer = 0
for i in range(2,n+1):
    #1이랑 부모가 같으면 answer +=1
    if Find(1)==Find(i):
        answer+=1
print(answer)