class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        # Example: nums = [1,1,2,2,3,3,4,5,6]

        while l < r:
            m = (l + r) // 2
            if m % 2 == 1:  # m is odd
                m -= 1      # make m even so it points to the start of a pair

            if nums[m] == nums[m + 1]:  
                # Pair is intact, so single element is after this pair
                l = m + 2
            else:  
                # Pair breaks here, so single element is at m or to the left
                r = m

        return nums[l]  # l == r at the end
