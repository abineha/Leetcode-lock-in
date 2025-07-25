class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        insert = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[insert] = nums[r]
                insert += 1
        
        return insert