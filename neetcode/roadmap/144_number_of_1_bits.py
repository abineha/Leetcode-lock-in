class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n :
            result += n % 2     # get last bit
            n = n >> 1          # right shift by 1
        return result
    
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         result = 0
#         while n :
#             n &= (n - 1)        # remove 1s 1 by 1
#             result += 1          
#         return result