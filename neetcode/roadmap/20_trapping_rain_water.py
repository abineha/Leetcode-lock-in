class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        
        result = 0
        l, r = 0, len(height) - 1 
        left_max, right_max = height[l], height[r]

        while l < r:
            if left_max < right_max:
                l+=1
                left_max = max(left_max, height[l])     # since updated left_max
                result+=left_max - height[l]    # never -ve
            else:
                r-=1
                right_max = max(right_max, height[r])
                result+=right_max - height[r]
        
        return result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))