import heapq

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        count = {}

        for n in hand:
            count[n] = 1 + count.get(n, 0)

        minHeap = list(count.keys())
        heapq.heapify(minHeap)
        
        while minHeap:
            first = minHeap[0]

            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:   # pop from minHeap
                    if i!= minHeap[0]:  # not da min val 
                        return False    # creates a hole in next group
                    heapq.heappop(minHeap)
        return True