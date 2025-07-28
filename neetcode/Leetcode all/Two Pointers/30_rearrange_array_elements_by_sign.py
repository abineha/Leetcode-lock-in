class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)
        pos, neg = 0, 1

        for n in nums:
            if n > 0:
                result[pos] = n
                pos += 2
            else:
                result[neg] = n
                neg += 2
        
        return result