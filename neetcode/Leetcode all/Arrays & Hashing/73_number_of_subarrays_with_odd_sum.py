class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        cur_sum = 0 
        even_cnt = 0
        odd_cnt = 0
        result = 0
        mod = 10**9 + 7

        for n in arr:
            cur_sum += n

            if cur_sum % 2:     # odd
                result = (result + even_cnt + 1) % mod
                odd_cnt += 1
            else:   # even
                result = (result + odd_cnt) % mod
                even_cnt += 1
        
        return result