# https://www.acmicpc.net/problem/1927
# 최소 힙
# 156ms python3 , library 사용시

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
            sys.stdout.write(str(heapq.heappop(heap))+"\n")
    else:
        heapq.heappush(heap,x)

'''
import sys

n = int(sys.stdin.readline().strip())  # 노드의 개수
heap = [0]*(n+1)
hn = 0 #heap size
def heapify(idx,size):
    l = idx*2
    r=idx*2+1
    max_i =idx
    if l<=size and heap[max_i]>heap[l]:
        max_i = l
    if r<=size and heap[max_i]>heap[r]:
        max_i = r
    if max_i != idx: #max_i가 idx와 달라지면 swap
        heap[idx], heap[max_i] = heap[max_i],heap[idx]
        heapify(max_i,size) 


def heap_sort(x):
    global hn

    heap[hn] = x
    hn += 1
    for i in range(hn//2-1,-1,-1):
        heapify(i,hn)


for _ in range(n):
    x = int(sys.stdin.readline().strip())
    print(_,heap)
    if x == 0:
        if hn == 0:
            print(0)
        else:
            print(heap.pop(0))
    else:
        heap_sort(x)
'''
