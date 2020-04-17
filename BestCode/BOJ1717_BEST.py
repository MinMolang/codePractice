# https://www.acmicpc.net/problem/1717
# 집합의 표현
# exponentialeecode ,288ms, python3(나는 1024ms pypy3인데..ㅜ)
import sys
n, m = map(int, sys.stdin.readline().split())

Set = [-1] * (n + 1)


def union(root1, root2):
    if Set[root2] < Set[root1]:
        Set[root2] += Set[root1]
        Set[root1] = root2
    else:
        Set[root1] += Set[root2]
        Set[root2] = root1


def find(i):
    if Set[i] < 0:
        return i
    else:
        Set[i] = find(Set[i])
        return Set[i]


for _ in range(m):
    t, a, b = map(int, sys.stdin.readline().split())
    if t == 1:
        if find(a) == find(b):
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")
    else:
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            union(root_a, root_b)

# wnsgur9648 ,336ms, pypy3(나는 1024ms pypy3인데..ㅜ)
import sys
input=sys.stdin.readline
print=sys.stdout.write
n,m=map(int,input().split())
p=[i for i in range(n+1)]
r=[0]*(n+1)
while m>0:
    o,a,b=map(int, input().split())
    while a != p[a]: a=p[a]
    while b != p[b]: b=p[b]
    if o: print("YES\n" if a==b else "NO\n")
    else:
        if a!=b:
            if r[a]<r[b]: p[a]=b
            else:
                p[b]=a
                if r[a]==r[b]: r[a]+=1
    m-=1
