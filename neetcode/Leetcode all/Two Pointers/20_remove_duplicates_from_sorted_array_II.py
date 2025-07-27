class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i, j = 0, 0

        while j < len(nums):
            d = nums[j]
            count = 0

            while j < len(nums) and nums[j] == d:
                j += 1
                count += 1
            
            nums[i] = d
            i += 1

            if count > 1:
                nums[i] = d
                i += 1
            
        return i