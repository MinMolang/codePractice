# 오답, pypy2, 샘플통과

import sys


def shortestPath(n, path, visited, currentLength):
    if len(path) == n:
        return currentLength

    res = 1416.0

    for next in xrange(0, n):
        if visited[next]: 
            continue

        here = path[-1] 
        path.append(next) 

        visited[next] = True

    
        candidate = shortestPath(n, path, visited, currentLength + dist[here][next])
        res = min(res, candidate)
        visited [next] = False 
        path.pop()


    return res


c =  int(sys.stdin.readline().strip())
for _ in range(c):


    n = int(sys.stdin.readline().strip())


    dist = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]



    answer = 1416.0

    for i in xrange(0,n):
        path = [i]
        visited = [False] * n
        visited[i] = True 
        res = shortestPath(n, path, visited, 0.0)

        if answer > res:
            answer = res

    print '%.10f\n' % answer 


