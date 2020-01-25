# https://www.acmicpc.net/problem/10866
# 덱구현

import sys

dq = []  # 큐 리스트
n = sys.stdin.readline()
for i in range(int(n)):
    sent = sys.stdin.readline()  # 괄호문자열,공백문자로 분리 push 1/ pop / empty / top
    sent = sent.strip().split()
    if sent[0] == 'push_front':
        dq.insert(0,sent[-1])
    elif sent[0] == 'push_back':
        dq.append(sent[-1])
    elif sent[0] == 'pop_front':
        if not dq:
            print(-1)
        else:
            print(dq.pop(0))
    elif sent[0] == 'pop_back':
        if not dq:
            print(-1)
        else:
            print(dq.pop())
    elif sent[0] == 'size':
        print(len(dq))
    elif sent[0] == 'empty':
        print(int(not dq))
    elif sent[0] == 'front':
        if not dq:
            print(-1)
        else:
            print(dq[0])
    elif sent[0] == 'back':
        if not dq:
            print(-1)
        else:
            print(dq[-1])


