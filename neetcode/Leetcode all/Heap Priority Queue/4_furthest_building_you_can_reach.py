from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        q = []

        for i in range(len(heights) - 1):
            dif = heights[i + 1] - heights[i]
            if dif <= 0:
                continue

            heapq.heappush(q, dif)

            if len(q) > ladders:
                bricks -= heapq.heappop(q)
                if bricks < 0:
                    return i

        return len(heights) - 1