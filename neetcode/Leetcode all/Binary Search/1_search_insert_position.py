class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        def search(l, r):
            if l > r:
                return l
            m = (l+r) // 2
            if target < nums[m]:
                return search(l, m-1)
            elif target == nums[m]:
                return m
            else:
                return search(m+1, r)
        
        return search(0, len(nums)-1)