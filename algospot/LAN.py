# # 입력
# 2
# 3 1
# 0 0 1
# 0 1 2
# 0 1
# 10 5
# -7 -7 10 -4 10 -4 -5 0 -10 -6
# 6 8 -5 3 -4 6 -10 4 -7 10
# 9 7
# 7 3
# 9 7
# 5 0
# 8 6

# 출력
# 1.4142135624
# # 29.7042202421

# only123님 풀이 참고

import sys
from itertools import combinations

rl = lambda: sys.stdin.readline().split()


# 주어진 그래프에 대해 최소 스패닝 트리에 포함된 간선의 목록을 selected에 저장하고, 가중치의 합을 반환
def prim():
    added = [False for _ in range(V)]
    minWeight = [float('inf') for _ in range(V)]  # 트리에 인접한 간선 중 해당 정점에 닿는 최소 간선의 정보를 저장
    parent = [-1 for _ in range(V)]
    ret = 0

    minWeight[0], parent[0] = 0, 0  # 0번 정점을 시작점으로 항상 트리에 가장 먼저 추가한다

    for _ in range(V):
        u = -1  # 다음에 트리에 추가할 정점 u를 찾는다

        for v in range(V):
            if not added[v] and (u == -1 or minWeight[u] > minWeight[v]):
                u = v

        ret += minWeight[u]
        added[u] = True

        # u에 인접한 간선(u,v)들을 검사한다
        for i in range(len(adj[u])):
            weight = adj[u][i]

            if not added[i] and minWeight[i] > weight:
                parent[i] = u
                minWeight[i] = weight

    return ret


for _ in range(int(input())):
    V, E = [int(x) for x in rl()]  # 건물의 수 N (N <= 500) 과 이미 설치된 케이블의 수 M (M <= 2000)

    x_coord = [int(x) for x in rl()]
    y_coord = [int(x) for x in rl()]
    adj = [[float('inf') for _ in range(V)] for _ in range(V)]  # 인접리스트 (연결된 정점 번호, 간선 가중치) 쌍

    for i, j in combinations(range(V), 2):
        adj[i][j] = adj[j][i] = ((x_coord[i] - x_coord[j]) ** 2 + (y_coord[i] - y_coord[j]) ** 2) ** 0.5  # 거리 구하기

    for _ in range(E):
        i, j = [int(x) for x in rl()]
        adj[i][j] = adj[j][i] = 0

    print(prim())
