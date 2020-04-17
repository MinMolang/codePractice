# https://www.acmicpc.net/problem/2805
# 나무 자르기
# 이진 탐색 트리
# python3 시간 초과, pypy3 768ms
import sys
n, m= list(map(int, sys.stdin.readline().split()))
h =  list(map(int, sys.stdin.readline().split()))

minh = 0; maxh = max(h)

while maxh>minh+1: #이진탐색 트리, 1개 차이가 날때까지 ex) [15,16]
    ch = (maxh+ minh)//2 #ouput 잘라야하는 높이를 일단 평균
    sum = 0 #가져가야하는 나무합
    for t in h:
        if t> ch:
            sum+= t-ch #ch보다 높은 나무들 자른 값들 더하기
    if sum>= m:
        minh = ch #최소값을 ch로 설정해서 다시 탐색
    else:
        maxh = ch #max를 ch값으로 설정해서 다시 탐색

print(minh) # [15,16] 1차이가 되었을 때는, while문을 벗어났고, 그때의 sum 계산되어있고, minh가 최적의 ch