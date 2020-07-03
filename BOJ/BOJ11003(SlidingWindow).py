# https://www.acmicpc.net/problem/11003
# 최소값찾기
# 덱 오름차준으로 저장
# (인덱스, 값)
# 맨 앞 인덱스와 현재 L 만큼 차이나는지 확인
# 맨 뒤에 있는 값이 현재 값보다 크면 삭제하고 현재 값을 덱에 넣는다.
import collections
import sys
ans = ''
n,l = map(int,sys.stdin.readline().strip().split())
a =  list(map(int,sys.stdin.readline().strip().split()))
al = len(a)
dq = collections.deque([])
for k in range(al):
   cur = a[k]
   if dq and dq[0][1]<=k-l:
       dq.popleft()
   while dq and dq[-1][0]>cur:
       dq.pop()
   dq.append((cur,k))
   ans+=str(dq[0][0])
   ans+=' '
print(ans[:-1])





