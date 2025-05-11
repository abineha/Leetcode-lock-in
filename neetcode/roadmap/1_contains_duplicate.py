class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        d={}
        for i in nums:
            ele=d.get(i,0)
            if ele!=0:
                return True
            else:
                d[i]=1
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1, 2, 3, 1]))