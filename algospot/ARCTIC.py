#코드출처 hunu님풀이

import sys
import math

#sys.stdin = open("input.txt")

def dfs(dists, power, visited, i):
    visited[i] = True
    for j, d in enumerate(dists[i]):
        if power >= d and not visited[j]:
            dfs(dists, power, visited, j)

def decision(dists, power):
    visited = [False] * len(dists)
    dfs(dists, power, visited, 0)
    for b in visited:
        if not b:
            return False
    return True

#이분탐색 
#모든 기지를 연결할 수 있는 최소의 d거리 반환 
def optimize(dists):
    hi = math.sqrt(1000.0 ** 2 + 1000.0 ** 2) + 1.0
    lo = 0.0
    while round(hi, 2) != round(lo, 2):
        mid = (hi + lo) / 2.0
#mid가 가능하면 더 좋은 답(작은)를 찾는다
        if decision(dists, mid):
            hi = mid
        else:
#mid가 불가능하면 더 나쁜답(큰)를 찾는다
            lo = mid
    return lo

C = int(input())
for _ in range(C):
    N = int(input())
    lines = [sys.stdin.readline().rstrip() for _ in range(N)]
    coords = list(map(lambda x: tuple(map(float, x.split())), lines))

    # dists[i, j] = distance between i-th and j-th coordinates.
    dists = [list() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            diff_x = coords[i][0] - coords[j][0]
            diff_y = coords[i][1] - coords[j][1]
            dist = math.sqrt(diff_x ** 2 + diff_y ** 2)
            dists[i].append(dist)

    min_power = optimize(dists)
    sys.stdout.write("{:.2f}\n".format(min_power))
