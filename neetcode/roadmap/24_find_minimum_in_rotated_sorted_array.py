class Solution:
    def findMin(self, nums: list[int]) -> int:
        mini = nums[0]
        l, r = 0, len(nums) - 1

        while l<=r:
            if nums[l] < nums[r]:
                mini = min(mini, nums[l])
                return mini
            m = (l+r)//2
            mini = nums[m]
            if nums[m] >= nums[l]:
                l = m +1
            else:
                r = r - 1
        
        return mini
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.findMin(nums = [3,4,5,1,2]))