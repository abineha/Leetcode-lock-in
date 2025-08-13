class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def can_split(largest):
            subarr = 0
            cur_sum = 0

            for n in nums:
                cur_sum += n
                if cur_sum > largest:
                    subarr += 1
                    cur_sum = n     # reset to new subarr having n
            
            return (subarr + 1) <= k

        l, r = max(nums), sum(nums)
        result = r  # set to max as we tryna minimize

        while l <= r:
            mid = (l+r) // 2
            if can_split(mid):
                result = mid
                r = mid-1
            else:
                l = mid+1
        
        return result