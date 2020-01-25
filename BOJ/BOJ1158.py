# https://www.acmicpc.net/problem/1158
# 요세푸스 문제
# 큐 활용 시뮬레이션
# 156ms

import sys

sent = sys.stdin.readline()  # 괄호문자열,공백문자로 분리 push 1/ pop / empty / top
n,k= map(int,sent.strip().split()) # sent[0] = 7 n명의 수, sent[-1] =3, 제거 번째, 포문활용
q = list(range(1,n+1))  # 큐 리스트
answer = "<"
# q가 empty가 될때까지
for j in range(n):
    this = (k-1)%len(q) # 이번회차 제거
    # print(this)
    if not q:
        break
    else:
        dead = q.pop(this)
        answer += str(dead)
        answer += ", "
        q = q[this:]+q[:this]

print(answer[:-2]+">")
#didwns7347's Code
n,k=map(int,input().split())
js=[ x for x in range(1,n+1)]
out=[]
i=k-1
for x in range(n):
    out.append(js.pop(i))
    if not js:
        break
    i=(i+k-1)%len(js)
print("<",end='')
for x in range(len(out)):
    if x==len(out)-1:
        print(out[x],end='')
    else:
        print(out[x],end=', ')
print(">")
