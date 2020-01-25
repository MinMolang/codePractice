# https://www.acmicpc.net/problem/16916
# 부분 문자열 구하기 _ Rabin-Karp Algorithm
# 836ms
def h(s):
    num = 0
    for c in s:
        num = (num * base + ord(c)) % mod
    return num


def match(s, p):
    n, m = len(s), len(p)
    if n<m:
        return 0
    first = 1
    for i in range(m-1):
        first = (first * base) % mod
    hash_p = h(p)
    hash_s = h(s[0:0 + m])
    for i in range(n - m+1):

        if hash_p == hash_s:
            return 1
        if i+m<n:
            hash_s = hash_s - (ord(s[i])*first)%mod
            hash_s = (hash_s+mod)%mod
            hash_s = ((hash_s*base)%mod+ord(s[i+m]))%mod

    return 0

import sys
mod = 2147483647
base = 256
s = sys.stdin.readline().strip() # strip 을 안해주면 whitespace가 들어감
p = sys.stdin.readline().strip()
print(match(s, p))
