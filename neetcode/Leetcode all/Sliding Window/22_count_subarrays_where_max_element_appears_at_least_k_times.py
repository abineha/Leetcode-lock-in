class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        max_ele, count = max(nums), 0
        l, result = 0, 0

        for r in range(len(nums)):
            if nums[r] == max_ele:
                count += 1
            
            while l <= r and count == k:
                count -= 1 if nums[l] == max_ele else 0
                result += (len(nums)-r)
                l += 1
        
        return result
