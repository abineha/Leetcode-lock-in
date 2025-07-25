class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i , j = 0, 0

        while i < len(nums) and j < len(nums):
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i+1, j+1
            elif nums[i] != 0:
                i, j = i+1, j+1
            else:
                j += 1
        
class Solution1:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

class Solution2:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert = 0
        for n in nums:
            if n:
                nums[insert] = n
                insert += 1
        
        for i in range(insert, len(nums)):
            nums[i] = 0