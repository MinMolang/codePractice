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

# 1.4142135624
# # 29.7042202421

# ref.  only123
import sys
from itertools import combinations


input = sys.stdin.readline

for _ in range(int(input())):
    V, E =  map(int, input().split())

    x_coord = list(map(int, input().split()))
    y_coord = list(map(int, input().split()))
    adj = [[0]*V for _ in range(V)]

    for i, j in combinations(range(V), 2):
        adj[i][j] = adj[j][i] = (x_coord[i] - x_coord[j]) ** 2 + (y_coord[i] - y_coord[j]) ** 2

    for _ in range(E):
        a, b = map(int, input().split())
        adj[a][b] = adj[b][a] = 0

    minWeight = [1e10]*V
    dist = minWeight[0] = 0.0
    added = [False]*V

    for _ in range(V):
        u = -1
        for i in range(V):
            if not added[i] and (u == -1 or minWeight[u] > minWeight[i]):
                u = i

        added[u] = True
        dist += minWeight[u] ** 0.5
        for i in range(V):
            if not added[i] and adj[u][i] < minWeight[i]:
                minWeight[i] = adj[u][i]

    print(dist)