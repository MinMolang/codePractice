# 입력
# 3
# 5
# -1000 -1000 -3 -1000 -1000
# 6
# 100 -1000 -1000 100 -1000 -1000
# 10
# 7 -5 8 5 1 -4 -8 6 7 9

# 출력
# -1000
# 1100
# 7

# 테스크 케이스1
# 현) 끝 2개 지우기 LEFT -3 -1000 -1000-1000
# 서) 왼쪽 끝에 2개 3 -1000 지우기   LEFT -1000
# 현) 2개 이하로 남아서 -1000을 가질 수 밖에 없다 

# 현 : -1000, 서: 0
# -1000

# 테스크 케이스2
# 현) 맨 왼쪽 100 선택
# 서) 맨 왼쪽 두개 지우기 LEFT  100 -1000 -1000
# 현) 맨 왼쪽 두개 지우기 LEFT  -1000
# 서) -1000을 가질 수 밖에 없다  

# 현 : 100, 서 : -1000
# 1100


#코드 출처 : only123님 풀이

def play(left, right):
    # 기저사례 : 모든 수가 다 없어졌을 때 
    if left > right:
        return 0
    
    ret = dp[left][right]
    if ret != EMPTY:
        return ret

    # 수를 가져가는 경우
    ret = max(board[left] - play(left + 1, right), board[right] - play(left, right - 1))
    
    # 수를 없애는 경우
    if right - left + 1 >= 2:
        ret = max(ret, -play(left+2, right))
        ret = max(ret, -play(left, right -2))
    
    dp[left][right] = ret
    return ret

for _ in range(int(input())):
    n = int(input())
    board = [int(x) for x in input().split()]
    EMPTY = -949327
    dp = [[EMPTY for _ in range(50)] for _ in range(50)]

    print(play(0, n-1))