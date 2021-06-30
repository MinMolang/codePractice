#  입력
# 2
# 6 3
# 40 3

# 출력
# 3 5
# 11 26

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().rstrip().split())
    survive = list(map(str, range(1, n + 1)))
    last_died_idx = 0
    survive.pop(0)
    # print(survive)
    while len(survive) > 2:
        next = (last_died_idx + k - 1) % len(survive)
        # print(next)
        survive.pop(next)
        last_died_idx = next

    print(' '.join(survive))
