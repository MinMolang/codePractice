# 입력
# 3
# ...
# ...
# ...
# xx.
# oo.
# ...
# xox
# oo.
# x.x

# 출력
# TIE
# x
# o

##jgd0423 님 풀이 참고

import sys
input = lambda : sys.stdin.readline()


# #boad를 아홉자리의 3진수 숫자로 본다 총 3^9 = 19683  (일대일 대응 함수)
def bijection(board):
    ret = 0
    for y in range(3):
        for x in range(3):
            ret = ret * 3
            if board[y][x] == 'o':
                ret = ret + 1
            elif board[y][x] == 'x':
                ret = ret + 2

    return ret


# 한 줄이 채워졌는지 확인하는 함수
def is_finished(board, turn):

    # 가로
    for y in range(3):
        for x in range(3):
            if board[y][x] != turn:
                break
            if x == 2:
                return True

    # 세로
    for y in range(3):
        for x in range(3):
            if board[x][y] != turn:
                break
            if x == 2:
                return True

    # 좌상우하 대각선
    for y in range(3):
        if board[y][y] != turn:
            break
        if y == 2:
            return True

    # 우상좌하 대각선
    for y in range(3):
        if board[y][2-y] != turn:
            break
        if y == 2:
            return True

    return False


def can_win(board, turn):
    opponent = 'o' if turn == 'x' else 'x'
    if is_finished(board, opponent):
        return -1

    int_board = bijection(board)
    if dp[int_board] != -2:
        return dp[int_board]

    min_value = 2
    for y in range(3):
        for x in range(3):
            if board[y][x] == '.':
                board[y][x] = turn
                min_value = min(min_value, can_win(board, opponent))
                board[y][x] = '.'

    if min_value == 2 or min_value == 0:
        dp[int_board] = 0
        return 0

    dp[int_board] = -min_value
    return -min_value


def find_start(board):
    empty = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                empty += 1
    
    return 'x' if empty % 2 == 1 else 'o'
        
for _ in range(int(input().strip())):
    board = []
    
    for _ in range(3):# 3*3 
        row = list(input().strip())
        board.append(row)
    
    dp = [-2 for _ in range(3 ** 9)] #boad를 아홉자리의 3진수 숫자로 본다 총 3^9 = 19683 
    
    start = find_start(board)
    ans = can_win(board, start)
    
    if ans == 1:
        print(start)
    elif ans == -1:
        print('o' if start == 'x' else 'x')
    elif ans == 0:
        print('TIE')