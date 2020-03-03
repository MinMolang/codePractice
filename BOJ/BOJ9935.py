# https://www.acmicpc.net/problem/9935
# 문자열 폭발
'''
mirkovC4nizCC44
C4


mirkovniz
'''

# 이문자의 특징은 스택을 활용 #c와 계속 비교해서 인덱스를  넣을 떄 튜플 s 인덱스와 같은 c 의 인덱스
import sys

s = sys.stdin.readline().strip() # 처음문자열
c  =  sys.stdin.readline().strip()
list = []

for x in range(len(s)):
    z = c.find(s[x])
    list.append((x,z))

print(list)