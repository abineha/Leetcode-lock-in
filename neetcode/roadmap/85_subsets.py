class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        subset = []     # current subset we building

        def dfs(i):     # ith element aka current index we're looking at
            if i >= len(nums):
                result.append(subset.copy())    # all the entries in result will point to the same list in memory but subset keeps changing
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            # decision not to include nums[i]
            subset.pop()
            dfs(i+1)

        dfs(0)
        return result
