# 샘플성공, 테스트 오답 (진행중)

# TODO
# board 받아오기 ok
# 테스트케이스 받아오기 ok
# board 5*5 돌면서 최초글자 해당하는지 확인ok
# board 상하좌우, 대각선 한칸씩 이동한 것과 두번째 글자 확인
# 글자수만큼 이동 ok
# 펜을 이동하지 않고 같은 글자 처리 ok
# 처음부터 못찾은 경우 NO 처리 ok
# check 변수만들고 YES NO 출력 ok
dx = [0,0,1,-1,-1,-1,1,1]
dy = [1,-1,0,0,1,-1,1,-1]

def move(x,y,test_case,curr):
  #print('x,y',x,y)
  if curr == len(test_case):
      return 'YES'
      
  for k in range(8):
    nx = x+dx[k]
    ny = y+dy[k]

    if 0<=nx<5 and 0<=ny<5: 
        #print(nx,ny)
        if not (x==nx and y==ny) and (board[nx][ny] == test_case[curr]):
            return move(nx,ny,test_case,curr+1)

c = int(input())
for _ in range(c):
  # 보글담기
  board = [list(input()) for _ in range(5)]

  # 테스트 케이스받아오기
  n = int(input())
  for _ in range(n):
    test_case = input()

    check = False
    for r in range(5):
      for c in range(5):
        if board[r][c] == test_case[0]:
          #이때부터만 다음 것들도 확인 가능
          x,y = r,c 
          #print('첫',r,c)
          ans = move(r,c,test_case,1)
          if ans == 'YES':
            check = True

    print(test_case,'YES' if check else 'NO')