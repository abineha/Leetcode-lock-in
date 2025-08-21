from typing import List
from collections import defaultdict
import heapq

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # Initialize result with -1 for all queries (default answer if no valid building is found)
        result = [-1] * len(queries)

        # Dictionary to group queries by their right index
        # groups[r] = [(required_height, query_index), ...]
        # Meaning: for query q_i, we need the first building (after r) taller than 'required_height'
        groups = defaultdict(list)

        # Step 1: Preprocess queries
        for i, q in enumerate(queries):
            l, r = sorted(q)  # Ensure l <= r for consistency

            # Case 1: If both indices are same → answer is r (same building)
            # Case 2: If building at r is already taller than building at l → answer is r
            if l == r or heights[r] > heights[l]:
                result[i] = r
            else:
                # Otherwise, we need to find the first building to the right of r
                # that is taller than max(heights[l], heights[r])
                h = max(heights[l], heights[r])
                groups[r].append((h, i))  # Store requirement with query index

        # Step 2: Sweep through all buildings from left to right
        min_q = []  # Min-heap storing queries waiting to be satisfied

        for i, h in enumerate(heights):
            # If some queries start at index i (their 'r' == i), push them into heap
            for q_h, q_i in groups[i]:
                heapq.heappush(min_q, (q_h, q_i))  

            # Process heap: while current building h satisfies the query (h > required_height)
            while min_q and h > min_q[0][0]:
                q_h, q_i = heapq.heappop(min_q)
                result[q_i] = i  # This building i is the first valid answer for query

        return result
