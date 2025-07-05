class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        map = {}
        for i in nums:
            map[i] = map.get(i, 0) + 1

        for i in range(len(nums)):
            if map.get(0, 0) != 0:
                nums[i] = 0
                map[0] -= 1
            elif map.get(1, 0) != 0:
                nums[i] = 1
                map[1] -= 1
            else:
                nums[i] = 2
