class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        def binary_search(l, r, target):    # return largest i where nums[i] < target (x)
            while l <= r:
                m = (l+r) // 2
                if nums[m] >= target:
                    r = m-1
                else:
                    l = m+1
                
            return r
        
        nums.sort()
        result = 0

        for i in range(len(nums)):
            low = lower - nums[i]
            up = upper - nums[i]
            result += (binary_search(i+1, len(nums)-1, up+1) - binary_search(i+1, len(nums)-1, low))
        
        return result
    
class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        def countLess(val: int) -> int:
            res, j = 0, len(nums) - 1
            for i in range(len(nums)):
                print(nums[i], nums[j])
                while i < j and nums[i] + nums[j] > val:
                    j -= 1
                res += max(0, j - i)
            return res

        nums.sort()
        return countLess(upper) - countLess(lower - 1)