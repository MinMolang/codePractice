# # 입력
# 1
# 7 14
# 0 1 1.3
# 0 2 1.1
# 0 3 1.24
# 3 4 1.17
# 3 5 1.24
# 3 1 2
# 1 2 1.31
# 1 2 1.26
# 1 4 1.11
# 1 5 1.37
# 5 4 1.24
# 4 6 1.77
# 5 6 1.11
# 2 6 1.2

# # 출력
# 1.3200000000

# only123 님 풀이 참고  

import sys
import heapq

def dijkstra(num):
    dist = [float('inf')] * N # 큰 수로 초기화
    dist[num] = 1
    heap = []
    heapq.heappush(heap, (1, num))

    while heap:
        cost, here = heapq.heappop(heap)

        # 만약 지금 꺼낸 것(cost)보다 더 짧은 경로를 알고 있다면 지금 꺼낸 것을 무시한다
        if dist[here] < cost:
            continue

        # 인접한 정점들을 모두 검사한다
        for there, c in adj[here]:
            next_dist = cost * c # 이 문제에서는 가중치의 합이 아니라 곱

            # 더 짧은 경로를 발견하면, dist[]를 갱신하고 heapq에 추가
            if dist[there] > next_dist:
                dist[there] = next_dist
                heapq.heappush(heap, (next_dist, there))

    return dist



for _ in range(int(input())):

    N, M = map(int, sys.stdin.readline().rstrip().split()) # 컴퓨터의 수 N (<= 10000) 과 회선의 수 M (<= 20000)
    adj = [[] for _ in range(N)] # 그래프의 인접 리스트 (연결된 정점 번호, 간선 가중치) 쌍을 담는다

    for _ in range(M): # 회선(간선) 수 만큼 추가
        a, b, c = sys.stdin.readline().rstrip().split()      # a와 b 회선의 노이즈 수 c
        a, b, c  = int(a), int(b), float(c)
        adj[a].append((b, c))
        adj[b].append((a, c))

    dist = dijkstra(0) # 첫번째 컴퓨터

    print('{0:.10f}'.format(dist[-1])) # 마지막 컴퓨터, 소숫점 및 열 자리까지 출력