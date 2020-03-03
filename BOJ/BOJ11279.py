# https://www.acmicpc.net/problem/11279
# 최대힙
# 192ms python3 , library 사용시
import sys
import heapq

n = int(sys.stdin.readline().strip())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if not heap:
            sys.stdout.write("0\n")
        else:
            sys.stdout.write(str(heapq.heappop(heap)[1])+"\n")
    else:
        heapq.heappush(heap,(-x,x))


'''
import sys

n = int(sys.stdin.readline().strip())  # 노드의 개수
heap = [0]*(n+1)
hn = 0 #heap size
def push(x):
    global hn
    hn+=1
    heap[hn] = x
    next = hn
    for i in range(hn, 1, -1):
        if i != next:
            continue
        else:

            if heap[i//2]<heap[i]:
                heap[i//2],heap[i] = heap[i],heap[i//2] #swap
                next = i // 2
            else:
                break

def pop():
    ans = heap[1] #인덱스 0부터가 아닌 1부터 시작
    global hn
    heap[1] = heap[hn] #루트를 가장 마지막에 있는 값으로
    # heap.pop(hn)
    heap[hn]=0
    hn-=1
    next = 1
    for i in range(1,hn+1):
        if i != next:
            continue
        else:
            if i*2<=hn:
                if heap[i] > heap[i * 2] and heap[i] > heap[i * 2 + 1]:  # 루트가 자식노드가 클 때,이상적인상황
                    break
                elif heap[i * 2] > heap[i * 2 + 1]:
                    heap[i], heap[i * 2] = heap[i * 2], heap[i]
                    next = i * 2
                else:
                    heap[i], heap[i * 2 + 1] = heap[i * 2 + 1], heap[i]
                    next = i * 2 + 1

            else:
                break

    return ans


for _ in range(n):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if hn == 0:
            print(0)
        else:
            print(pop())
    else:
        push(x)




'''
