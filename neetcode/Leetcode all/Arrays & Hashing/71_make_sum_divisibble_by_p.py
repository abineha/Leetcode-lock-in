class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        total = sum(nums)
        remain = total % p

        if remain == 0:
            return 0

        result = len(nums)
        remain_map = { 0 : -1 }
        cur_sum = 0
        
        for i, n in enumerate(nums):
            cur_sum = (cur_sum + n) % p
            prefix = (cur_sum - remain + p) % p

            if prefix in remain_map:
                length = i - remain_map[prefix]
                result = min(result, length)
            
            remain_map[cur_sum] = i

        return -1 if result == len(nums) else result