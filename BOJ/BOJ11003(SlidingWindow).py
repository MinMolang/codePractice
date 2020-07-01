# https://www.acmicpc.net/problem/11003
# 최솟값찾기

import sys
ans = ''
n,l = map(int,sys.stdin.readline().strip().split())
a =  list(map(int,sys.stdin.readline().strip().split()))
al = len(a)
for k in range(1,al+1):
   if k-l+1<=0:
       first = 0
   else:
       first = k-l+1-1
   last = k
   ans+=str(min(a[first:last]))
   ans+=' '
print(ans[:-1])




