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

#코드출처: https://doriri.tistory.com/33 [My Programming]


def find_word_st(dx, dy, test_case, index):
    for (x, y) in xy:
        if dy + y > 4 or dy + y < 0 or dx + x > 4 or dx + x < 0:
            continue

        if board[dy + y][dx + x] is test_case[index]:
            if length is index + 1:
                return True
            if find_word_st(dx + x, dy + y, test_case, index + 1) is True:
                return True


def find_word_ch(test_case):
    global length
    length = len(test_case)

    for dy in range(0, 5):
        for dx, ch in enumerate(board[dy]):
            if test_case[0] is ch:
                if find_word_st(dx, dy, test_case, 1) is True:
                    return "YES"

    return "NO"


c = int(input())
for _ in range(c):
    # 보글담기
    board = [list(input()) for _ in range(5)]

    # 테스트 케이스받아오기
    n = int(input())
    for _ in range(n):
        test_case = input()

        print(test_case, find_word_ch(test_case))
