# 3
# 3 7
# #.....#
# #.....#
# ##...##
# 3 7
# #.....#
# #.....#
# ##..###
# 8 10
# ##########
# #........#
# #........#
# #........#
# #........#
# #........#
# #........#
# ##########

# 풀이
# 3의 배수가 아닐 경우 답이 없다.
# 흰 칸의 수를 3으로 나눠서 내려놓은 블록의 수 N을 얻은 뒤, 문제의 답을 생성하는 과정을 N조각으로 나눠 한 조각에서 한블록을 내려놓도록 한다.
# 재귀함수는 주어진 게임판에 블록을 한 개 내려놓고 난뒤 남은 흰 칸들을 재귀 호출을 이용해 덮도록 한다
# 중복을 방지하기 위해 가장 위쪽 가장 왼쪽에 있는 칸을 덮는 것이라고 강제한다
# 블록은 4가지가 노올 수 있다.
# 남은 게인판을 다시 재기 호출로 넘긴다

#TODO
# 입력구현 OK
# 흰색 구간 찾아보기
import sys

# 칸을 덮을 수 있는 네가지 방법
# 블록을 구성하는 세칸의 상대적 위치 (dy, dx)
coverType = [[[0, 0], [1, 0], [0, 1]], [[0, 0], [0, 1], [1, 1]], [[0, 0], [1, 0], [1, 1]], [[0, 0], [1, 0], [1, -1]]]

# board(y,x)를 type번 방법으로 덮거나, 덮었던 블록을 없앤다
# delta 1 덮고, -1이면 덮었던 블록을 없앤다
# 블록이 제대로 덮이지 않은 경우 (게임밖, 겹치거나, 검은 칸) -> false 반환

def set(board, y, x, type, delta):
    ok = True
    for i in range(3):
        ny = y + coverType[type][i][0]
        nx = x + coverType[type][i][1]
        if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board[0]):
            ok = False
        # board[ny][nx] += delta
        elif (board[ny][nx] + delta) >1:
            board[ny][nx] += delta
            ok = False
    return ok

# board의 모든 빈 칸을 덮을 수 있는 방법의 수를 반환하다
# board[i][j] = 1 이미 덮인 칸 혹은 검은칸
# board[i][j] = 0 아직 덮이지 않은 칸
def cover(board):
    # 아직 채우지 못한 칸 중 가장 윗줄 왼쪽에 있는 칸을 찾는다
    y, x = -1, -1
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                y, x = i,j
                break
        if y!= -1: # 어떤 의미인지 아직 파악하지 못함
            break

# 기저사례 : 모든 칸을 채웠으면 1을 반환
    if y == -1 :
        return 1
    ret = 0 #의 역할은?
    for type in range(4):
        # 만약 board[y][x]를 type 형태로 덮을 수 있으면 재귀 호출한다
        if set(board, y, x, type, 1):
            ret += cover(board)

        # 덮었던 블록을 치운다
        set(board, y, x, type, -1)
    return ret



n = int(input())
for _ in range(n):
  # H,W 입력
  h,w = sys.stdin.readline().strip().split()
  h,w = int(h), int(w)

  #board판입력
  origin = [input() for _ in range(h)]
  copy = [[0]*w for _ in range(h)]
  for r in range(h):
      for c in range(w):
          if origin[r][c] != '#':
              copy[r][c] == 1


  print(origin)
  ans = cover(copy)
  print(ans)