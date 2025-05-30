import heapq

class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        intervals.sort()
        minHeap = []
        result, i = {}, 0

        for q in sorted(queries):   # need original order of queries to return, so create a copy
            while i < len(intervals) and intervals[i][0] <= q:  # add interval < q
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))   
                i += 1

            while minHeap and minHeap[0][1] < q:    # right value of interval
                heapq.heappop(minHeap)

            result[q] = minHeap[0][0] if minHeap else -1         

        return [ result[q] for q in queries]