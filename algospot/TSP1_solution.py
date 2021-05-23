# py3 최종
# 입력
# 2
# 3
# 0.0000000000  611.6157225201  648.7500617289
# 611.6157225201  0.0000000000  743.8557967501
# 648.7500617289  743.8557967501  0.0000000000
# 4
# 0.0000000000  326.0008994586  503.1066076077  290.0250922998
# 326.0008994586  0.0000000000  225.1785728436  395.4019367384
# 503.1066076077  225.1785728436  0.0000000000  620.3945520632
# 290.0250922998  395.4019367384  620.3945520632  0.0000000000

# 출력
# 1260.3657842490
# 841.2045646020

# 코드 출처  saxycow님 py3코드
# TODO
# 입력 ok
# 소수 처리 ok
# 재귀 구현, 안가본 곳 모든 경우의 수 찾기

import sys

# 안 가본 곳들을 재귀로 방문하면서 가장 짧은 길이를 반환
# here : 현재 도시
# currentLength : 지금까지 만든 경로의 길이
def shortestPath(here, currentLength):
    global num_visited
    global cost
    #기저사례 : 거리가 너무 크면 미리 종료
    if currentLength > cost:
        return INF

    #기저사례 : 모든 도시 방문 종료
    if num_visited == n:
        return currentLength

    # 다른 도시들도 방문
    for city, val in enumerate(dist[here]): #해당하는 도시 행만 실행
        if not visited[city]: # 방문하지 않은 도시 방문
            visited[city] = True
            num_visited += 1
            cost = min(cost, shortestPath(city,currentLength + val))
            visited[city] = False # 다시 초기화, 중요!!
            num_visited -= 1

    return cost

c =  int(sys.stdin.readline().strip())
for _ in range(c):

    # 테스트 케이스받아오기
    n = int(sys.stdin.readline().strip())

    # 거리담기
    dist = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]
    visited = [False] * n
    num_visited = 0
    INF = 987654321

    #최대값으로 초기화
    g_cost = INF

    for i in range(0,n):
        cost = g_cost
        visited[i] = True # 출발했으므로 방문 체크!! 중요!! 오답원인!!
        num_visited = 1
        g_cost = min(g_cost, shortestPath(i, 0.0))
        visited[i] = False

    print(g_cost)


