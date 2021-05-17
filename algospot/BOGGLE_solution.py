# 1
# URLPM
# XPRET
# GIAET
# XTNZY
# XOQRS
# 6
# PRETTY
# GIRL
# REPEAT
# KARA
# PANDORA
# GIAZAPX

# PRETTY YES
# GIRL YES
# REPEAT YES
# KARA NO
# PANDORA NO
# GIAZAPX YES

# 실패한 예제
# 1
# NNNNN
# NEEEN
# NEYEN
# NEEEN
# NSNNN
# 1
# YES


# TODO
# board 받아오기 ok
# 테스트케이스 받아오기 ok
# board 5*5 돌면서 최초글자 해당하는지 확인ok
# board 재귀호출하며 단어가 있는지 확인 
dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]


def hasWord(y, x, test_case):
    #print(y,x)
    # 기저사례1. 시작 위치가 범위 밖이면 무조건 실패
    if y < 0  or y > 4 or x < 0 or x > 4:
      #print('t1')
      return False
    
    boolean = (test_case[0]==board[y][x])
    test_case = test_case[1:]
    
    if boolean:
      if not(len(test_case)):
        # 빈경우
        #print('t2')
        return True
      else:
        #print('t4')
        #인접한 여덟 칸을 검사한다.
        for k in range(8):
          #다이나믹 프로그래밍
            nx = x + dx[k]
            ny = y + dy[k]
        
            if hasWord(ny, nx, test_case):
              return True
    else:
      #print('t5')
      return False


c = int(input())
for _ in range(c):
    # 보글담기
    board = [list(input()) for _ in range(5)]

    # 테스트 케이스받아오기
    n = int(input())
    for _ in range(n):
        test_case = input()
        
        ans = False
        
        for r in range(5):
          for c in range(5):
             ans = hasWord(r, c, test_case)
             if ans:
               break
          if ans:
            break
          
            
        
        print(test_case, 'YES' if ans else 'NO')
