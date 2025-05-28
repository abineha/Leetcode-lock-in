# just sort

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]
    
# Quick sort - TLE

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        k = len(nums) - k   # index if sorted, kth largest

        def quick_select(l, r):  # portion of array -> quick select
            pivot, pointer = nums[r], l  # last ele as pivot
            
            for i in range(l, r):   # except last index as it is pivot
                if nums[i] <= pivot:
                    nums[pointer], nums[i] = nums[i], nums[pointer]   # swap, less than pivot eles to the left
                    pointer += 1    # next position

            nums[pointer], nums[r] = nums[r], nums[pointer]

            if pointer > k:   # target index < p, quick select on left (small indexes)
                return quick_select(l, pointer - 1)
            elif pointer < k:
                return quick_select(pointer + 1, r)   #right portion
            else:
                return nums[pointer]   # pointer is the kth largest ele
        
        return quick_select(0, len(nums) - 1)
    