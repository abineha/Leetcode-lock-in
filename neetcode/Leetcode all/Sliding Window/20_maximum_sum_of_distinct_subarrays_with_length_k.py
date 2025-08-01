class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        l, result, sum = 0, 0, 0
        hash = set()

        for r in range(len(nums)):
            while nums[r] in hash:
                hash.remove(nums[l])
                sum -= nums[l]
                l += 1
            
            hash.add(nums[r])
            sum += nums[r]

            if (r-l+1) > k:
                sum -= nums[l]
                hash.remove(nums[l])
                l += 1

            if (r-l+1) == k:
                result = max(result, sum)
        
        return result

class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        l, result, sum = 0, 0, 0
        prev_idx = {}

        for r in range(len(nums)):
            sum += nums[r]
            i = prev_idx.get(nums[r], -1)

            while l <= i or (r-l+1) > k:
                sum -= nums[l]
                l += 1

            if (r-l+1) == k:
                result = max(result, sum)

            prev_idx[nums[r]] = r
        
        return result