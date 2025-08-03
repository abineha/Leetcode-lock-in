from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        count = defaultdict(int)
        result = 0
        L1, L2 = 0, 0

        for r in range(len(nums)):
            count[nums[r]] += 1

            while len(count) > k:
                count[nums[L2]] -= 1
                if count[nums[L2]] == 0:
                    count.pop(nums[L2])
                L2 += 1
                L1 = L2
            
            while count[nums[L2]] > 1:
                count[nums[L2]] -= 1
                L2 += 1
            
            if len(count) == k:
                result += (L2 -L1 +1)
        
        return result