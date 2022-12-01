from heapq import heappush, heappop

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        heap = []
        
        for room in sorted(intervals):
      
            if heap and room[0] >= heap[0]:
                heapq.heappushpop(heap, room[1])
            else:
                heapq.heappush(heap, room[1])

        return len(heap)
