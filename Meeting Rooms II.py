#  Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required. Input: intervals = [(0,30),(5,10),(15,20)]
# Output: 2
# Explanation:
# We need two meeting rooms
# room1: (0,30)
# room2: (5,10),(15,20)

def minMeetingRooms(self, intervals):
    if len(intervals) == 0:
        return 0
    intervals = sorted(intervals, key=lambda x: x.start)
    import heapq
    heap = []
    heapq.heappush(heap, intervals[0].end)
    for i in range(1, len(intervals)):
        if intervals[i].start < heap[0]:
            heapq.heappush(heap, intervals[i].end)
        else:
            heapq.heappop(heap)
            heapq.heappush(heap, intervals[i].end)
    return len(heap)