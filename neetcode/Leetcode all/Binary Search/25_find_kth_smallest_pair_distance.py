from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # Count how many pairs (i < j) have nums[j] - nums[i] <= dist
        def count_pairs_le(dist: int) -> int:
            l = 0
            total = 0
            # r sweeps right; l only moves right (two-pointer)
            for r in range(len(nums)):
                # Keep the window valid: smallest index l such that
                # nums[r] - nums[l] <= dist
                while nums[r] - nums[l] > dist:
                    l += 1
                # All i in [l, r-1] form valid pairs with r -> (r - l) pairs
                total += r - l
            return total

        nums.sort()

        # Search distance in [0, max possible distance]
        # Using nums[-1]-nums[0] is the tightest upper bound after sorting.
        lo, hi = 0, nums[-1] - nums[0]

        # Binary search the smallest distance with at least k pairs
        while lo < hi:
            mid = (lo + hi) // 2
            if count_pairs_le(mid) >= k:
                hi = mid      # mid works; try smaller
            else:
                lo = mid + 1  # mid too small; need larger distance

        return lo  # or hi; lo == hi here
