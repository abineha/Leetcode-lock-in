from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        """
        Return the minimal 'capability' c such that we can choose k elements
        from nums with no two chosen elements adjacent, and every chosen
        element is <= c.
        """

        def valid(capability: int) -> bool:
            """
            Greedy check: can we pick k non-adjacent elements with value <= capability?
            We scan left-to-right; whenever we find nums[i] <= capability we pick it
            (count++), and skip the next element (i += 2) to enforce non-adjacency.
            """
            i = 0
            count = 0
            n = len(nums)

            while i < n:
                if nums[i] <= capability:
                    # Pick this element and skip its neighbor
                    count += 1
                    i += 2
                else:
                    # Can't pick this element, move to next index
                    i += 1

                # If we've already reached k picks, no need to continue
                if count == k:
                    break

            return count == k

        # Binary-search over the capability value.
        # Lower bound is min(nums), upper bound is max(nums)
        l, r = min(nums), max(nums)
        result = r  # initialize with upper bound (safe default)

        while l <= r:
            m = (l + r) // 2
            # If we can pick k elements with capability m, try smaller capability
            if valid(m):
                result = m
                r = m - 1
            else:
                # Otherwise, need larger capability
                l = m + 1

        return result
