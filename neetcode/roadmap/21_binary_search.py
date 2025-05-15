class Solution:
    def binarysearch(self, l: int, r: int, nums:list[int], target:int) -> int:
        if l > r:
            return -1
        m = l + (r -l)//2 # overflow safe
        if nums[m] == target:
            return m
        elif nums[m] < target:
            return self.binarysearch(m+1,r,nums,target)
        return self.binarysearch(l,m-1,nums,target)

    def search(self, nums: list[int], target: int) -> int:
        return self.binarysearch(0, len(nums) - 1, nums, target,)
    
# iterative soln
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l, r = 0, len(nums) - 1

#         while l <= r:
#             # (l + r) // 2 can lead to overflow
#             m = l + ((r - l) // 2)  

#             if nums[m] > target:
#                 r = m - 1
#             elif nums[m] < target:
#                 l = m + 1
#             else:
#                 return m
#         return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.search(nums = [-1,0,3,5,9,12], target = 9))