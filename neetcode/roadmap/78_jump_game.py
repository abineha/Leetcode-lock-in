class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1 # reach last index
        
        for i in range(len(nums) - 1, -1, -1):  # reverse order traversal
            if i + nums[i] >= goal:  # can reach goal
                goal = i    # shift goal closer to left

        return True if goal == 0 else False