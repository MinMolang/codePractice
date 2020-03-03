# https://www.acmicpc.net/problem/1717
# 집합의 표현
# stdinstdout 수정 1048ms -  840ms
# 마지막 따로 저장 없이 바로 write 840ms - 776ms*****
# 딕셔너리를 사용하지 않고 if else write 하면 800ms
# rank를 없앰 776ms - 532ms
# union 중복함수를 뺐는데.. 근데 증가했네.. 580ms
# union 내부 수정/python3 308ms
# 딕셔너리 전역변수로 빼니까 300ms ***

import sys

n,m= map(int,sys.stdin.readline().split())
parent = [-1]*(n+1)
ans = {True: 'YES', False: 'NO'}

def Find(x):
    if parent[x]<0: #union 진행이후에도 부모가 된 녀석들 음수가 되어, 더이상 find 해주지 않음
        return x
    else:
        parent[x] = Find(parent[x])
        return parent[x]

def Union(x,y): #일단 여기에는 부모의 인덱스가 들어옴
    if parent[y] < parent[x]:
        parent[y] += parent[x]
        parent[x] = y
    else:
        parent[x] += parent[y]
        parent[y] = x

for _ in range(m):
    __,a,b = map(int,sys.stdin.readline().split())
    sys.stdout.write(str(a)+str(b)+str(parent)+"\n")
    if __ == 0:
        root_a = Find(a)
        root_b = Find(b)
        if root_a != root_b:
            Union(root_a, root_b)
    else:
        sys.stdout.write(ans[Find(a) == Find(b)]+"\n")