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

# 코드 출처 : https://junho-one.tistory.com/2
import sys

# 칸을 덮을 수 있는 네가지 방법
# 블록을 구성하는 세칸의 상대적 위치 (dy, dx)
move = [[(0, 0), (0, 1), (1, 0)], [(0, 0), (0, 1), (1, 1)], [(0, 0), (1, 0), (1, 1)], [(0, 0), (1, 0), (1, -1)]]

def firstEmpty():
  for x in range(H):
      for y in range(W):
          if matrix[x][y] == '.':
              return x, y

  return -1, -1


def checkBlock(x, y, num):

  for dx, dy in move[num]:

      nx = x + dx
      ny = y + dy

      if not (0 <= nx < H and 0 <= ny < W):
          return False

      if matrix[nx][ny] == '#':
          return False

  return True


def fillBlock(x, y, num):

  for dx, dy in move[num]:
      nx = x + dx
      ny = y + dy
      matrix[nx][ny] = '#'


def removeBlock(x, y, num):

  for dx, dy in move[num]:
      nx = x + dx
      ny = y + dy
      matrix[nx][ny] = '.'


def countBlock():

  x, y = firstEmpty()

  if x is -1 and y is -1:
      return 1

  ret = 0

  for m in range(len(move)):
      if checkBlock(x, y, m):
          fillBlock(x, y, m)
          ret += countBlock()
          removeBlock(x, y, m)

  return ret




n = int(input())
for _ in range(n):
  # H,W 입력
  H,W = map(int, sys.stdin.readline().rstrip().split(" "))


  #board판입력
  matrix = [list(sys.stdin.readline().rstrip()) for _ in range(H)]

  white = 0
  for r in range(H):
      for c in range(W):
          if matrix[r][c] == '.':
              white +=1


  # 3의 배수 체크
  if white % 3 == 0:
    ans = countBlock()
    print(ans)
  else:
    print(0)
