# https://programmers.co.kr/learn/courses/30/lessons/42626#qna
# 더 맵게
# 문의롤 통해 scoville 지수의 길이는 모두 2 이상으로 변경!
# 따라서 scoville지수의 길이가 1이면서 이미 k 이상인 경우는 존재x
import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    size = len(scoville)
    for t in range(size-1):
        one = heapq.heappop(scoville)
        two = heapq.heappop(scoville)
        new = one+(two*2)
        heapq.heappush(scoville,new)
        answer+=1
        if scoville[0]>=K:
            return answer
    return -1


