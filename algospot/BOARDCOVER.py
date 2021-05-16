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

# 고민되는 부분
# 서로 다른 방법에 대한 표현, 어떻게 블록이 조금이라도 다르게 덮었는지 표현할 수 있을까
# 방법 1) L 개체마다 다른 숫자를 입력해준다. 111/222/333/444
# 다음번에 확인할 때, 내가 높으려고 시도하는 곳이 똑같이 111로 입력되어있으면 패스 112, 이렇게 일부가 달라지게 되면 , 새로운 숫자 999 이렇게 입력하고 방법의 수 CNT+1
# 한 번 다 채우기 전에 CNT를 한번만 올리도록 유의

# 고민되는 부분2
# .이 다 안채워지너가 다른걸로채워졌다는 것을 매번 어떻게 확인해줄지
# 일차배열로 흰부분만 넣얺고 .이 존재하는지 검사?

# 유의사항
#서로 겹치거나, 검은 칸을 덮거나, 게임판 밖으로 나가서는 안 됩니다
#TODO
# 입력구현 OK
# 흰색 구간 찾아보기
import sys
n = int(input())
for _ in range(n):
  # H,W 입력
  h,w = sys.stdin.readline().strip().split()
  h,w = int(h), int(w)

  #board판입력
  origin = [input() for _ in range(h)]
  #copy = [[0]*w for _ in range(h)]
  print(origin)
  #print(copy)

  # 일단 흰색이 있는 곳을 찾아볼까
  white_list = []
  color = 1
  for r in range(h):
      for c in range(w):
          if origin[r][c] != '#':
              white_list.append((r,c))
              a,b,c = check(r,c,origin)

              #해당하는 경우라면
              if a[0]!= -1:
                origin[a[0]][a[1]] = color
                origin[b[0]][a[1]] = color
                origin[c[0]][c[1]] = color
                color+=1

  # 한개도 없을 경우 1처리
  if not white_list:
      print(1)



  print(white_list)
