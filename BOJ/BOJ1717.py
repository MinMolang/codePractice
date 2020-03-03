# https://www.acmicpc.net/problem/1717
# 집합의 표현
# 1048ms, PyPy3

import sys

n,m= map(int,sys.stdin.readline().strip().split())
edge = [[] for x in range(n+1)]  #0부터 n까지 n+1개 존재
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
for _ in range(m):
    __,a,b = map(int,sys.stdin.readline().strip().split())
    if __ == 0:
        Union(a, b)
    else:
        ans = {True : 'YES',False:'NO'}
        print(ans[Find(a) == Find(b)])