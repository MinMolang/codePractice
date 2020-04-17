import sys
n= int(sys.stdin.readline().strip())
li = list(map(int,sys.stdin.readline().strip().split()))
print(n,li)
booth = {}
left = 0 #왼쪽에 위치한 1의 인덱스
right = 1000000
zero = []
one = []
for idx,x in enumerate(li):
    if x==0:
        zero.append(idx)
    elif x==1:
        one.append(idx)
print(zero,one)
# zero를 가지고 우리는 예상할 수 있지
k  = 0
for x in range(1,len(zero)):
    if zero[x]-zero[x-1]==1:
        print(1)
    else:
        pass
