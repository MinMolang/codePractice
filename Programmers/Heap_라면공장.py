# https://programmers.co.kr/learn/courses/30/lessons/42629
# 효율성 2,3 시간초과
import heapq
def solution(stock, dates, supplies, k):
    answer = 0
    heap = []
    dateidx= 0
    for i in range(k):
        #1) 밀가루 공급받는 날이고, 아직 여유가 있을 때
        if  dateidx<len(dates) and dates[dateidx]==i: #꼭 len를 먼저 앞에서 체크
            heapq.heappush(heap,(-supplies[dateidx],supplies[dateidx]))
            dateidx+=1
        #2) stock이 다 떨어진 날
        if stock == 0:
            stock+=heapq.heappop(heap)[1]
            answer+=1
        stock-=1
    return answer