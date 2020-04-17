# https://www.acmicpc.net/problem/1463
# 1로 만들기
# 다이나믹 프로그래밍
# 564ms
n = int(input())

d = [0 for _ in range(n+1)] # 최소 수 저장 d = [0]*(n+1) , n+1까지*

for i in range(2,n+1):
    d[i] = d[i-1]+1
    if i%2 == 0 and d[i]>d[i//2]+1: #정수만 가능 / 대신 //
        d[i] = d[i // 2] + 1
    if i%3 == 0 and d[i]>d[i//3]+1:
        d[i] = d[i // 3] + 1
print(d[n])