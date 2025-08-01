class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        l, count = 0, 1
        result = []

        for r in range(len(nums)):
            if r > 0 and nums[r-1] + 1 == nums[r]:
                count += 1
            if (r-l+1) > k:
                if nums[l] + 1 == nums[l+1]:
                    count -= 1
                l += 1
            if (r-l+1) == k:
                result.append(nums[r] if count == k else -1)
        
        return result