class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:     
        result= []
        nums.sort()
        print(nums)
        for i, v in enumerate(nums):
            if v > 0:
                break  # positive numbers wont add up to 0

            if i > 0 and v == nums[i-1]:
                continue  # current a in (a,b,c) is duplicated skip

            l, r = i+1, len(nums) - 1
            while l < r:
                threesum = v + nums[l] + nums[r]
                if threesum > 0:
                    r-=1
                elif threesum < 0:
                    l+=1
                else:
                    result.append([v, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return result

    
if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum(nums = [-1,0,1,2,-1,-4]))