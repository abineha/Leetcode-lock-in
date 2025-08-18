import heapq
from typing import List

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # Step 1: Normalize the array
        # - If a number is odd, multiply it by 2 (because odd numbers can only increase).
        # - If a number is even, keep it as is (since it can be halved later).
        # - Use negative values because Python's heapq is a min-heap by default, 
        #   and we want to simulate a max-heap.
        q = list(set(-(x*2 if x % 2 == 1 else x) for x in nums))

        # Step 2: Build a heap from the numbers
        heapq.heapify(q)

        # Step 3: Initialize max and min values
        # - max_v = largest value currently in heap (since heap stores negatives, take -q[0])
        # - min_v = smallest value across the heap (convert negatives back)
        max_v = -q[0]
        min_v = -max(q)

        # Initial deviation (difference between max and min values)
        deviation = max_v - min_v

        # Step 4: Keep reducing the maximum value if it is even
        # Because even numbers can be divided by 2 to reduce deviation
        while q[0] % 2 == 0:
            # Remove the largest element (stored as negative, so it's at heap[0])
            new_v = heapq.heappop(q) // 2   # divide it by 2 (still negative)

            # Push the reduced value back into heap
            heapq.heappush(q, new_v)

            # Update max_v (largest element in heap, so -q[0])
            max_v = -q[0]

            # Update min_v as the minimum seen so far
            # (-new_v is the positive value of the one we just added)
            min_v = min(min_v, -new_v)

            # Update deviation
            deviation = min(deviation, max_v - min_v)
        
        # Step 5: Return the minimum deviation found
        return deviation
