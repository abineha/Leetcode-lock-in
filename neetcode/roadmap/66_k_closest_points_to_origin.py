import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[List[int]]:
        minHeap = []
        for x, y in points:
            d = ( x**2 + y**2)  # calc distance from origin
            minHeap.append([d, x, y])

        heapq.heapify(minHeap)
        result = []

        while k > 0:
            d, x, y = heapq.heappop(minHeap)
            result.append([x, y])
            k -= 1
               
        return result