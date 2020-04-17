'''
5 2
4
3
5
2
8

14
'''
# ​첫째 줄에 손님 그룹의 개수 N 과 문을 연 매표소 K 가 정수로 주어진다.
# 둘째 줄 부터 N 줄 만큼 각 그룹의 손님수가 유니에게 도착한 순서대로 주어진다. 그룹은 입력된 순서대로 매표소에 줄을 선다.
import sys
n, k = list(map(int, sys.stdin.readline().strip().split()))
group = []
for _ in range(n):
    gn = int(sys.stdin.readline().strip())
    group.append(gn)
print(n,k,group)
# 자 이제...
# group[0]..
# group[0]%k ==0
# cnt + group[0]// 시간 추가
# 만약 group[0]k != 0
# group[0]%k 나머지를 다음에 더하고
# 의 반복
ans = 0
booth = {}
for x in range(k):
    if group:
        booth[x] = group.pop(0)
    else:
        break

for one in group:
    midx = 1000000 #큰 수 입력
    akey = 1000000 #큰 수 입력 할 것 
    for key,value in booth.items():
        if value<midx:
            midx = value
            akey = key
    print(midx,akey)
    booth[akey]+=one
print(max(booth.values()))
    #
    # [x for x in ans if x > 0]
    # lambda x, y: x + y,



# cnt = 0

# for it in range(len(group)):
#         group[it]-=1

