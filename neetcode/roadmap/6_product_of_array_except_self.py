class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res=[1]*len(nums)
        prefix=1
        postfix=1
        for i in range(len(nums)):
            res[i]*=prefix
            prefix*=nums[i]
            res[-1-i]*=postfix
            postfix*=nums[-1-i]
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf(nums = [1,2,3,4]))

