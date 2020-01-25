# https://www.acmicpc.net/problem/10828
# 스택구현

import sys #여러줄을 읽기 위해서
#STACK 연결리스트 구현체 참고 https://wayhome25.github.io/cs/2017/04/18/cs-20/
class Stack:
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def is_empty(self):
        # print("eee", self.stack)
        if not self.stack:
            return 1
        return 0
    def top(self):
        # print("ttt", self.stack)
        if not self.stack:
            return -1
        return self.stack[-1]

    def pop(self):
        # print("ppp",self.stack)
        if not self.stack:
            return -1
        return self.stack.pop()

n = sys.stdin.readline()
s = Stack()
for i in range(int(n)):
    sent = sys.stdin.readline() # 괄호문자열,공백문자로 분리 push 1/ pop / empty / top
    sent = sent.strip().split()
    if sent[0] == 'push':
        s.push(sent[-1])
    elif sent[0] == 'pop':
        print(s.pop())
    elif sent[0] == 'size':
        print(len(s.stack))
    elif sent[0] == 'top':
        print(s.top())
    elif sent[0] == 'empty':
        print(s.is_empty())

#
#

