import heapq
from typing import List

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        people = [(p, i) for i, p in enumerate(people)]
        result = [0] * len(people)
        count = 0
        start, end = [f[0] for f in flowers], [f[1] for f in flowers]
        heapq.heapify(start)
        heapq.heapify(end)

        for p, i in sorted(people):
            while start and start[0] <= p:
                heapq.heappop(start)
                count += 1

            while end and end[0] < p:
                heapq.heappop(end)
                count -= 1
            
            result[i] = count
        
        return result
    
import heapq
from typing import List

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # Pair each person with their index so we can return results in original order later
        people = [(p, i) for i, p in enumerate(people)]
        
        # Initialize result array with zeros
        result = [0] * len(people)
        
        # Sort flowers by start time
        flowers.sort()
        
        # Min-heap to store flower end times (the soonest-ending flower stays on top)
        end = []
        
        # Pointer to iterate through flowers
        j = 0

        # Process people in sorted order (ascending time)
        for p, i in sorted(people):
            
            # Add all flowers that have started blooming by time `p`
            while j < len(flowers) and flowers[j][0] <= p:
                heapq.heappush(end, flowers[j][1])  # push flower's end time
                j += 1

            # Remove flowers that have already ended before `p`
            while end and end[0] < p:
                heapq.heappop(end)

            # The heap now contains only flowers that are blooming at time `p`
            result[i] = len(end)
        
        return result
