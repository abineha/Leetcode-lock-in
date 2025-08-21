import heapq
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        result = float("inf")
        pairs = []  # (wage-to-quality ratio, quality)

        # Step 1: Build pairs of (ratio, quality)
        for i in range(len(quality)):
            # ratio = wage[i]/quality[i]
            # This means worker i demands at least "ratio * quality" wage
            pairs.append((wage[i]/quality[i], quality[i]))
        
        # Step 2: Sort workers by their wage-to-quality ratio (ascending)
        pairs.sort(key=lambda p: p[0])

        max_q = []   # max heap (to store largest qualities, negated for min-heap behavior)
        total_q = 0  # sum of selected qualities

        # Step 3: Iterate through workers sorted by ratio
        for r, q in pairs:
            # Add this worker’s quality to heap and update total quality
            heapq.heappush(max_q, -q)   # push -q so heap acts like max-heap
            total_q += q

            # If we have more than k workers, remove the one with the largest quality
            if len(max_q) > k:
                total_q += heapq.heappop(max_q)  # pop removes -q (largest q), so add it back to total_q

            # If we have exactly k workers, compute cost
            if len(max_q) == k:
                # cost = (sum of qualities) * (current ratio)
                # Because the current ratio is the max ratio in the group (sorted order)
                result = min(result, total_q * r)
        
        return result
