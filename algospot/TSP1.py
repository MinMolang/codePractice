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

# 1260.3657842490
# 841.2045646020

# TODO
# 입력 ok
# 소수 처리 ok
# 재귀 구현, 안가본 곳 모든 경우의 수 찾기

import sys

def travel(visited, min_val):
    global n
    # 다 방문했으면 종료
    if len(n) == len(visited):
      return min_val
    
    # 새롭게 방문
    # 최소값 갱신
    for i in range(1, n):
      if i not in visited:
        travel(visited.append(i), min_val)
    
    

c = int(input())
for _ in range(c):
    # 테스트 케이스받아오기
    n = int(input())
    # 거리담기
    dist = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]
    print(dist)

    min_val = 1416
  # 최초시작 0의 거리로 시작, 0,0 과 0,1 / 0,0 과 0,2 이렇게 구하는visited에 넣는다
    result = []
    for i in range(1, n):
      res = travel([0,i], min_val)
      result.append(res)
  
    print(min(result))
