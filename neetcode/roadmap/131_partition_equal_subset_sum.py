class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2 == 1:  # odd cant be partitioned
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums)-1, -1, -1):
            nextdp = set()
            for t in dp:
                if (t+nums[i]) == target:
                    return True
                nextdp.add(t+nums[i])
                nextdp.add(t)
            dp = nextdp        

        return True if target in dp else False