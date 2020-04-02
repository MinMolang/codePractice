# https://www.acmicpc.net/problem/7562

import sys

dx = [1, 2, 2,1,-1,-2,-2,-1]
dy = [-2, -1,1,2,2,1,-1,-2]

test = int(sys.stdin.readline().strip())
for k in range(test):
    ans = 0
    sqr = int(sys.stdin.readline().strip())
    board= [[-1]*sqr for x in range(sqr)]
    fx,fy = map (int,sys.stdin.readline().strip().split())
    tx,ty = map (int,sys.stdin.readline().strip().split())
    q = []
    q.append((fx, fy))
    board[fx][fy] = 0
    while q:
        x = q[0][0]
        y = q[0][1]
        q.pop(0)
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < sqr and 0 <= ny < sqr:
                if board[nx][ny] == -1 :
                    board[nx][ny] = board[x][y] + 1
                    q.append((nx, ny))
    print(board[tx][ty])

