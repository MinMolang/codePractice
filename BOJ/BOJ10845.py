# https://www.acmicpc.net/problem/10845
# 큐 구현
#back은 list 특성상 -1로 혹은 back = 0 으로 한뒤, push해줄때, back+=1
#front는 항상 0, python list에서 항상 pop(0)을 해줄 것이라서
import sys
q = []  # 큐 리스트
n = sys.stdin.readline()
for i in range(int(n)):
    sent = sys.stdin.readline()  # 괄호문자열,공백문자로 분리 push 1/ pop / empty / top
    sent = sent.strip().split()
    if sent[0] == 'push':
        q.append(sent[-1])
        # back+=1
    elif sent[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.pop(0))
    elif sent[0] == 'size':
        print(len(q))
    elif sent[0] == 'empty':
        print(int(not q))
    elif sent[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif sent[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])