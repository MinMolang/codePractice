xy = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
]

#코드출처: aksndk123님 코드

def has_word(x, y, index):
    global board, str_len, xy, test_case, visit
    if board[x][y] != test_case[index]:
        return 0
    elif board[x][y] == test_case[index] and index == str_len - 1:
        return 1
    else:
        visit[x][y][index] = 1
        for dx, dy in xy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and index + 1 < str_len and visit[nx][ny][index + 1] == 0:
                if has_word(nx, ny, index + 1):
                    return 1
    return 0

c = int(input())
for _ in range(c):
    # 보글담기
    board = [list(input()) for _ in range(5)]

    # 테스트 케이스받아오기
    n = int(input())
    for _ in range(n):
        test_case = input()
        str_len = len(test_case)
        visit = [[[0] * str_len for _ in range(5)] for ___ in range(5)]
        flag = 0
        for i in range(5):
            for j in range(5):
                if has_word(i, j, 0):
                    flag = 1
                    break
            if flag == 1:
                break
        if flag:
            print(test_case + " YES")
        else:
            print(test_case + " NO")
