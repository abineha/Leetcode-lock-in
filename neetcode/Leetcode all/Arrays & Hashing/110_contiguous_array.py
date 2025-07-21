class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        zero, one = 0, 0
        result = 0
        dif_idx = {}    # count[1] - count[0] = index

        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else: 
                one += 1
            
            if (one-zero) not in dif_idx:
                dif_idx[one-zero] = i
            
            if one == zero:
                result = one+zero
            else:
                idx = dif_idx[one-zero]
                result = max(result, i-idx)
        
        return result