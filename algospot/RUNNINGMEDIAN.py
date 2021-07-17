# 주어진 수열을 두 묶음으로 나눔
# 숫자들을 정렬한 뒤, 앞의 절반을 최대 힙, 뒤의 절반을 최소 힙
# 홀수라면 최대 힙에 숫자를 하나 더 넣도록

# 이것을 다음과 같은 두 개의 불변식
# 1. 최대 힙의 크기는 최소 힙의 크기와 같거나 하나 더 크다
# 2. 최대 힙의 최대 원소는 최소 힙의 최소 원소보다 작거나 같다

# 수열의 중간 값은 항상 최대 힙의 루트에
# 만약 2. 조건이 만족하지 않는다면 최대 힙의 최대원소와 최소 힙의 최소 원소를 맞바꿈

# 입력
# 3
# 10 1 0
# 10 1 1
# 10000 1273 4936

# 출력
# 19830
# 19850
# 2448920

# 힙을 이용
# s__b__2 님 풀이 참조
import heapq as hq

for i in range(int(input())):
    N, a, b = map(int, input().split())
    min_hq = []
    max_hq = [-1983]
    val = 1983
    sum = 1983

    for j in range(N - 1):

        val = (val * a + b) % 20090711

        # 수열의 길이가 홀수면 최대 힙에 숫자를 하나더
        if len(min_hq) == len(max_hq):
            hq.heappush(max_hq, -val)
        else:
            hq.heappush(min_hq, val)

        # 최대 힙의 최대 원소와 최소 힙의 최소 원소보다 작거나 같다
        if -max_hq[0] > min_hq[0]:
            t1 = -hq.heappop(max_hq)
            t2 = -hq.heappop(min_hq)
            hq.heappush(max_hq, t2)
            hq.heappush(min_hq, t1)

        sum += -max_hq[0]

    print(sum % 20090711)

