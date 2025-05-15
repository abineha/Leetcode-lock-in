class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r) // 2
            if (nums[m] == target):
                return m
            
            # left sorted portion ?
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1   # search right
                else:
                    r = m - 1  # search left

            else: #right sorted portion
                if target < nums[m] or target > nums[r]:
                    r = m - 1  # search left
                else:
                    l = m + 1    # search right
 
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.search(nums = [4,5,6,7,0,1,2], target = 0))