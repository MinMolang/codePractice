# https://www.acmicpc.net/problem/11048
# 이동하기
# O(NM)
# 다이나믹 프로그래밍, 대각선 아래로의 이동은 0<=사탕의개수이기 때문에, 계산하지 않아도 됨! 아래로, 오른쪽을 거쳐서 가는 경로가 항상 많다

import sys

n,m= list(map(int,sys.stdin.readline().strip().split()))
# 0말고 1부터 인덱스 시작, 따라서 0행 0열 추가
a = [[0]*(m+1)]+[[0]+list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]
sweet = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        sweet[i][j] = max(sweet[i-1][j],sweet[i][j-1])+a[i][j]

print(sweet[n][m])