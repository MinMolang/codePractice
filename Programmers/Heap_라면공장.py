# https://programmers.co.kr/learn/courses/30/lessons/42629
# 출처 https://codedrive.tistory.com/82
import heapq
def solution(stock, dates, supplies, k):
    answer = 0
    heap = []
    dateidx = 0
    ldates = len(dates)
    while stock<k:
        for i in range(dateidx,ldates):
            if dates[i]<=stock:
                heapq.heappush(heap,(-supplies[i],supplies[i]))
                dateidx=i+1
            else:
                break
        stock+=heapq.heappop(heap)[1]
        answer+=1
    return answer