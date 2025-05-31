class Solution:
    def jump(self, nums: list[int]) -> int:
        result = 0
        l = r = 0   # sliding window, lvl for BFS

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            result += 1     # no. of jumps
        return result