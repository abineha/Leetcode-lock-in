class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longset=set(nums)
        long=0
        for i in nums:
            if (i -1) not in longset:
                leng=0
                while (i+leng) in longset:
                    leng+=1
                long=max(long,leng)
        return long

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive(nums = [100,4,200,1,3,2]))