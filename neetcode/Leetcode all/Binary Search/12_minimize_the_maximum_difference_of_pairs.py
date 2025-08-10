from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        """
        Given nums and an integer p, form exactly p disjoint pairs
        (no shared elements) such that the maximum difference among
        chosen pairs is minimized.
        """

        def valid(threshold: int) -> bool:
            """
            Check if it's possible to form at least p pairs such that
            the absolute difference of each pair is <= threshold.
            We greedily form pairs from left to right after sorting.
            """
            i = 0
            count = 0
            n = len(nums)

            while i < n - 1:  # need at least two elements to make a pair
                # Since nums is sorted, nums[i+1] is the closest number to nums[i]
                if abs(nums[i] - nums[i + 1]) <= threshold:
                    # Form a pair (i, i+1)
                    count += 1
                    i += 2  # skip both elements
                else:
                    i += 1  # try next index

                if count == p:  # early exit if we have enough pairs
                    return True

            return False  # not enough pairs formed

        # Edge case: if no pairs are required
        if p == 0:
            return 0

        # Sort numbers so closest elements are adjacent
        nums.sort()

        # Binary search boundaries:
        # 0 is smallest possible max difference
        # max(nums) - min(nums) is the largest possible max difference
        l, r = 0, max(nums) - min(nums)
        result = r  # start with the largest possible

        # Binary search for the minimum threshold that works
        while l <= r:
            m = (l + r) // 2  # candidate threshold

            if valid(m):
                result = m  # record possible answer
                r = m - 1   # try to find smaller threshold
            else:
                l = m + 1   # need a bigger threshold

        return result
