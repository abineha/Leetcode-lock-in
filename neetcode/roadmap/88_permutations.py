class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 0:
            return [[]]     # base case: 1 permutation of empty list
        
        perms = self.permute(nums[1:])  # insert 1st ele last
        result = []

        for p in perms:
            for i in range(len(p) + 1):   # index position at which to add 1st ele
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                result.append(p_copy)

        return result