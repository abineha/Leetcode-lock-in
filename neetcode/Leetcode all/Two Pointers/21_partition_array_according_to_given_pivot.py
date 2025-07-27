class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        i, j = 0, len(nums)-1
        x, y = 0, len(nums)-1
        result = [0] * len(nums)

        while i < len(nums):
            if nums[i] < pivot:
                result[x] = nums[i]
                x += 1
            if nums[j] > pivot:
                result[y] = nums[j]
                y -=1

            i, j = i+1, j-1
        
        while x <= y:
            result [x] = result[y] = pivot
            x, y = x+1, y-1

        return result