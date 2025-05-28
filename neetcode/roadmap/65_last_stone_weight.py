import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-s for s in stones]   # no maxheap so -ve values in minheap
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)    # 1st largest stone
            second = heapq.heappop(stones)   # 2nd largest stone
            if second > first:
                heapq.heappush(stones, first - second)   # -2,-3 so -2 + 3 => +ve

        stones.append(0)
        return abs(stones[0])