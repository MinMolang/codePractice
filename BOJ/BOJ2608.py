# https://www.acmicpc.net/problem/16922
# 로마숫자만들기

n = int(input())
check = []
#3중 포문
# 0~ n개 까지 check, 0 은 사용 x
for i in range(n+1):
    for v in range(n+1):
        for x in range(n+1):
            l = n - i-v-x
            if l <0:
                continue
            value = i*1+v*5+x*10+l*50
            if value not in check:
                check.append(value)
print(len(check))