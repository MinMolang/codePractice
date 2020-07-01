#숫자의 길이는 10개, 사용할 수 있는 1,2,3,4 개
# K번째 경우의 수

import sys
k = int(sys.stdin.readline().strip())
cnt = 0
def process () :
    global cnt
    cnt +=1
    if cnt==k:
        print(' '.join(map(str, arr)))
    pass
def recursion(idx):
    if idx>=10:
        process()
        return

    for k in range(1,5):
        arr[idx] = k
        recursion(idx+1)







arr = [0]*10
recursion(0)