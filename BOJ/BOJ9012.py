# https://www.acmicpc.net/problem/9012
# 괄호

n = input()
for i in range(int(n)):
    sent = input()  # 괄호문자열
    ssize = 0
    for k in sent:
        if ssize==-1:
            break
        elif k == '(':
            ssize+=1
        else:
            ssize-=1

    if ssize == 0:
        print('YES')
    else:
        print('NO')
