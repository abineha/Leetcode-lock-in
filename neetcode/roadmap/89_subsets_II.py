class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                result.append(subset.copy())
                return
            # INCLUDE ELE
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            # DOESNT INCLUDE ELE
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, subset)
        
        backtrack(0, [])
        return result