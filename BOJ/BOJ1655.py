# https://www.acmicpc.net/problem/1655
# 가운데를 말해요
# 힙 사용
'''
10
1
5
2
10
-99
7
5
1
3
4
'''
import sys
import heapq
n  =  int(sys.stdin.readline().strip())

ln,rn = 0,0
l,r = [],[]

def l_change(x):
    global ln, rn
    _,it = heapq.heappop(l)
    ln -= 1
    heapq.heappush(r,it)
    rn+=1
    heapq.heappush(l, (-x, x))
    ln += 1


def r_change(x):
    global ln, rn

    it = heapq.heappop(r)
    rn -= 1
    heapq.heappush(l,(-it,it))
    ln+=1
    heapq.heappush(r, x)
    rn += 1




#     왼쪽의 최댓값을 계속 pop해와서
# 이번에 들어올 값과 비교하면서
# 이번에 들어올값과 같아질때까지
# 미연의 방지한다
# 일단 그러면 들어올값을 왼쪽에 보낸뒤 3 2
# 팝한값을 오른쪽에 보내고 2 3
def check(x):
    global ln, rn
    if ln==rn:     # 왼쪽의 개수가 오른쪽의 개수랑 같다면
        b = r[0]
        if b>=x:     # 숫자값에 따라 왼오 들어갈 곳을 판단
            heapq.heappush(l,(-x,x))
            ln+=1
        else:
            heapq.heappush(r,x)
            rn+=1
    elif ln<rn:     # 오른쪽의 개수가 1개 더 많다면
        # 왼쪽에 들어가야 하는데...
        # 왼쪽에 들어가려하는데 왼쪽의 최댓값보다는 크지만 오른쪽의 최솟값보다는 큰 상황이면
        if r[0] < x:
            r_change(x)

        else:
            heapq.heappush(l, (-x,x))
            ln += 1
    elif rn<ln:     # 왼쪽의 개수가 1개 더 많다면
        # 오른쪽에 들어가야하긴하는데..
        # 오른쪽에 들어가려하는데 오른쪽의 최솟값보다 작지만 왼쪽의 최댓값보다 큰 상황이라면
        # 대공사가 필요한 상황
        if r[0]>x:
            l_change(x)

        else:
            heapq.heappush(r, x)
            rn += 1

    # 왼쪽힙의 최댓값과 오른쪽 힙의 최솟값과 비교
    # process를 비교
    # 왼쪽의 개수가 오른쪽의 개수랑 같다면
    # 숫자값에 따라 왼오 들어갈 곳을 판단
    # 왼쪽의 개수가 1개 더 많다면
    # 무조건 오른쪽에 들어가야하낟.
    # 오른쪽의 개수가 1개 더 많다면
    # 무조건 왼쪽으로 들어가야하낟.
    # 예외 상황의 경우 , 이동시켜야하는 경우

for _ in range(1,n+1):
    k = int(sys.stdin.readline().strip())

    if _ == 1:
        heapq.heappush(l, (-k, k))
        ln += 1
        sys.stdout.write(str(l[0][1]) + "\n")
    elif _==2:
        heapq.heappush(r, k)
        rn+=1
        if l[0][1]<=k:
            sys.stdout.write(str(l[0][1]) + "\n")
        else:
            sys.stdout.write(str(k) + "\n")
    else:
        check(k)
        if _%2 ==0: #짝수인경우는 항상 왼쪽힙에서
             sys.stdout.write(str(l[0][1])+"\n")
        else:
            if ln<rn:#오른쪽힙의 수가 많으면 최소힙
                sys.stdout.write(str(r[0]) + "\n")
            else:#왼쪽힙의 수가 많으면 최대힙
                sys.stdout.write(str(l[0][1]) + "\n")



