# https://www.acmicpc.net/problem/16916
# 부분 문자열 구하기 _ KMP Algorithm
# 596ms
import sys
def preprocessing(p):
    m = len(p)
    # print(m)
    pi = [0 for i in range(m)]
    j = 0
    for i in range(1,m):
        while j>0 and p[i]!=p[j]: j=pi[j-1]
        if p[i]==p[j]:
            pi[i] = j+1 # fail 함수에 +1해서 저장
            j+=1
        else:
            pi[i] = 0 #fail함수에 0으로 입력
    return pi
def kmp(s, p):
    n, m = len(s), len(p)
    # 맞은경우1
    pi = preprocessing(p)
    # print("pi : ",pi)
    ans = []
    j = 0
    for i in range(0,n):
        # print("for", i, j)
        while j>0 and s[i] !=p[j]:
            j = pi[j-1]
            # print("while",i,j)


        if s[i]==p[j]:
            if j == m-1:
                ans.append(i-m+1)
                # j=pi[j]
                # print("ifif",i,j)
            else:
                j+=1
                # print("ifelse", i, j)
    # 틀린경우 0
    if not ans:
        return 0
    else:
        return 1
s =  sys.stdin.readline().strip()
p =  sys.stdin.readline().strip()

print(kmp(s,p))