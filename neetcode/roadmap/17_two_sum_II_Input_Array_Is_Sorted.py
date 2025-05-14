class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        while(l<r):
            sum = numbers[l] + numbers[r]
            if sum < target:
                l+=1
            elif sum > target:
                r-=1
            else:
                return [ l + 1, r + 1 ]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum(numbers = [2,7,11,15], target = 9))