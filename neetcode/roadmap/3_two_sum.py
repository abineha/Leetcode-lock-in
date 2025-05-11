class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d={}
        for i in range(len(nums)):
            diff=target-nums[i]
            ele=d.get(diff,-1)
            if(ele!=-1):
                return [d[diff],i]
            else:
                d[nums[i]]=i

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum(nums = [2,7,11,15], target = 9))