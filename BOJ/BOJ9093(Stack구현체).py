#https://www.acmicpc.net/problem/9093
#단어뒤집기 문제


# 풀이. t에서 for 문개수를 받아오고
#     공백문자가 마주치면
#     이전 stack 문제를 pop하고
#     새로운 스택들을 공백 안에 넣어준다.
    # 중요한 것은  \n 개행문자도 고려해주어야한다.
    # 개행문자를 만났을 때도 pop 해주어야하기 때문에

class Stack(list):
    push = list.append

    def is_empty(self):
        if not self:
            return True
        else:
            return False
    def top(self):
        return self[-1]


n = int(input())
for x in range(n):
    sent = input()
    sent += " "
    s = Stack()
    answer = ''
    for char in sent:
        if char == ' ' or char == '\n':
            while(not s.is_empty()):
                it = s.pop()
                answer += it
            answer+=' '
        else:
            s.push(char)
    print(answer)





