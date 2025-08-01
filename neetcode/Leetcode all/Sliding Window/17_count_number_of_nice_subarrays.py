class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        def atMost(k):
            l = res = 0
            for r in range(len(nums)):
                if nums[r] % 2 == 1:
                    k -= 1
                while k < 0:
                    if nums[l] % 2 == 1:
                        k += 1
                    l += 1
                res += (r - l + 1)
            return res

        return atMost(k) - atMost(k - 1)

class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        result, odd = 0, 0
        l, m = 0, 0
        
        for r in range(len(nums)):
            if nums[r] % 2:
                odd += 1
            while odd > k:
                if nums[l] % 2:
                    odd -= 1
                l += 1
                m = l
            if odd == k:
                while nums[m] % 2 == 0:
                    m += 1
                result += (m-l) + 1
        
        return result