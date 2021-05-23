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

# 코드 출처 https://jaimemin.tistory.com/304
# TODO
# 입력 ok
# 소수 처리 ok
# 재귀 구현, 안가본 곳 모든 경우의 수 찾기

import sys

# 안 가본 곳들을 재귀로 방문하면서 가장 짧은 길이를 반환
# path : 지금까지 만든 경로
# visited : 각 도시 방문 여부
# currentLength : 지금까지 만든 경로의 길이
def shortestPath(n, path, visited, currentLength):
    #기저사례 : 모든 도시 방문 종료
    if len(path) == n:
        return currentLength

    res = 1416.0

    # 다른 도시들도 방문
    for next in range(0, n):
        if visited[next]: # 이미 방문
            continue

        here = path[-1] # 최초 시작은 0
        path.append(next) # 방문하고자 하는 도시 추가

        visited[next] = True

        # 나머지 경로를 재귀 호출을 통해 완성하고 가장 짧은 경로의 길이를 얻는다
        global dist
        candidate = shortestPath(n, path, visited, currentLength + dist[here][next])
        res = min(res, candidate)
        visited [next] = False # 다시 초기화, 중요!!
        path.pop()


    return res


c = int(input())
for _ in range(c):

    # 테스트 케이스받아오기
    n = int(input())

    # 거리담기
    dist = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]


    #최대값으로 초기화
    answer = 1416.0

    for i in range(0,n):
        path = [i]
        visited = [False] * n
        visited[i] = True # 출발했으므로 방문 체크!! 중요!! 오답원인!!
        res = shortestPath(n, path, visited, 0.0)

        if answer > res:
            answer = res

    print(answer)


