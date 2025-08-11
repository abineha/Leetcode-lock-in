class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        # Lower_bound: first index i such that nums[i] >= target.
        # Uses [l, r) convention with r = n so we can return n when no element >= target.
        def binarySearch(target):
            l, r = 0, n
            while l < r:
                m = l + (r - l) // 2
                # If nums[m] is >= target, the answer is at m or left of m
                if nums[m] >= target:
                    r = m
                else:
                    # nums[m] < target -> answer must be right of m
                    l = m + 1
            return l  # l == r == lower_bound

        # find first index >= target
        start = binarySearch(target)

        # if start is out of range or the value at start isn't target, target doesn't exist
        if start == n or nums[start] != target:
            return [-1, -1]

        # end = last index equal to target = first index >= target+1 minus 1
        end = binarySearch(target + 1) - 1
        return [start, end]
