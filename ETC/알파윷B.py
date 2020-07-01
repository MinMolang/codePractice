# 5
# 2 3 1 2 4

import sys
n = int(sys.stdin.readline())
board = list(map(int,sys.stdin.readline().strip().split()))
score = [0,5, 10 ,15,20,50,30,35,40,45,100,55,60,65,70,75,80,85,90,95,500,1000]
curr = 0

answer = ''
for t in board:
    curr += t
    if curr>=21:
        curr = 21
    print("%d " % score[curr],end = '')

    if curr ==21:
        break


'''
import sys
n = int(sys.stdin.readline())
board = list(map(int,sys.stdin.readline().strip().split()))
score = [0,5, 10 ,15,20,50,30,35,40,45,100,55,60,65,70,75,80,85,90,95,500,1000]
curr = 0

answer = ''
for t in board:
    curr += t
    if curr<22:
        answer += str(score[curr])
        answer += ' '
    else:
        answer += str(score[-1])
        answer += ' '
        break

print(answer[:-1])
'''