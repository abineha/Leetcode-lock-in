from collections import Counter

# extra space memory
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        length = len(nums)
        if length <= 1:
            return nums
        else:
            pivot = nums.pop()
        items_lower, items_greater = [], []
        for i in nums:
            if i > pivot:
                items_greater.append(i)
            else:
                items_lower.append(i)
        
        return self.sortArray(items_lower) + [pivot] + self.sortArray(items_greater)
        
# Counting sort
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        cnt = Counter(nums)
        ans = []
        
        for i in range(min(cnt.keys()), max(cnt.keys())+1):
            if i not in cnt:
                continue
            else:
                freq = cnt[i]
                while freq > 0:
                    ans.append(i)
                    freq -= 1

        return ans

# leetcode only accepts this quick sort idk why
from random import randint

class Solution:
    def QuickSort(self, nums, left, right):
        if left >= right:
            return
        pivot = randint(left, right)
        nums[pivot], nums[right] = nums[right], nums[pivot]  # put pivot at end
        l, r = left, right - 1
        pivot_val = nums[right]

        while l <= r:
            while l <= r and nums[l] < pivot_val:
                l += 1
            while l <= r and nums[r] > pivot_val:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        nums[l], nums[right] = nums[right], nums[l]  # put pivot in its correct position

        self.QuickSort(nums, left, l - 1)
        self.QuickSort(nums, l + 1, right)

    def sortArray(self, nums: list[int]) -> list[int]:
        self.QuickSort(nums, 0, len(nums) - 1)
        return nums

