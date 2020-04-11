# https://programmers.co.kr/learn/courses/30/lessons/42626#qna
# 더 맵게
import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville:
        if scoville[0] >= K:
            return answer
        one = heapq.heappop(scoville)
        two = heapq.heappop(scoville)
        new = one + (two * two)
        heapq.heappush(scoville, new)
        answer += 1

    return -1