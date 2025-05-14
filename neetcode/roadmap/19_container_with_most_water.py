# # BRUTE FORCE O(n^2)
# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#         result = 0 

#         for l in range(len(height)):
#             for r in range(l+1, len(height)):
#                 area = (r-l)* min(height[l], height[r])  # lower height as it decides water being contained 
#                 result = max(area, result)
#         return result
    
# OPTIMAL O(n)
class Solution:
    def maxArea(self, height: list[int]) -> int:
        result = 0 
        l, r = 0, len(height)-1
        while l<r:
            area = (r-l)* min(height[l], height[r])  # lower height as it decides water being contained 
            result = max(area, result)
            if height[l] <= height[r]:
                l+=1
            else:
                r-=1

        return result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea(height = [1,8,6,2,5,4,8,3,7]))