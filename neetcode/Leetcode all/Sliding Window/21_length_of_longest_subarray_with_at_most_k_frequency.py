from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        l, result = 0, 0
        hash = defaultdict(int)

        for r in range(len(nums)):
            hash[nums[r]] += 1

            while hash[nums[r]] > k:
                hash[nums[l]] -= 1
                l += 1
            result = max(result, r - l + 1)

        return result