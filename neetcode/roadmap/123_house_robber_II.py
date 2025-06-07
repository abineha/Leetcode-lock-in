class Solution:
    def rob(self, nums: list[int]) -> int:

        return max(nums[0], self.rob1(nums[1:]), self.rob1(nums[:-1]))  # nums[0] cause if only 1 ele? except 1st ele, except last ele

    def rob1(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0
         
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2