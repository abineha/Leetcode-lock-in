class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        insert = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[insert], nums[i] = nums[i], nums[insert]
                insert += 1
        
        return nums