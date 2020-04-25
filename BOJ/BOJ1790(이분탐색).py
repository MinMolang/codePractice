# https://www.acmicpc.net/problem/1790
# 수 이어쓰기 2
import sys

n, k= list(map(int, sys.stdin.readline().split()))
print(n,k)

mink = 1; maxk = n
for x in range(1,n+1):
    if x<10:
        pass
# while maxk>mink+1: #이진탐색 트리, 1개 차이가 날때까지 ex) [15,16]

'''
 ch = (maxh+ minh)//2 #ouput 잘라야하는 높이를 일단 평균
    sum = 0 #가져가야하는 나무합
    for t in h:
        if t> ch:
            sum+= t-ch #ch보다 높은 나무들 자른 값들 더하기
    if sum>= m:
        minh = ch #최소값을 ch로 설정해서 다시 탐색
    else:
        maxh = ch #max를 ch값으로 설정해서 다시 탐색
'''

print(minh)