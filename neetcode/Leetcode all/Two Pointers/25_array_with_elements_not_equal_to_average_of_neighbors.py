class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        # WIGGLE
        # [0] > [1] < [2] > [3] < ...
        # or
        # [0] < [1] > [2] < [3] > ...

        inc = nums[0] < nums[1]
        for i in range(1, len(nums)-1):
            if ( inc and nums[i] < nums[i+1]) or ( not inc and nums[i] > nums[i+1]):
                nums[i], nums[i+1] = nums[i+1], nums[i]
            inc = not inc
        return nums