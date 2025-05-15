from typing import List

# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         if not matrix or not matrix[0]:
#             return False
        
#         rows, cols = len(matrix), len(matrix[0])
#         left, right = 0, rows * cols - 1
        
#         while left <= right:
#             mid = left + (right - left) // 2
#             mid_value = matrix[mid // cols][mid % cols]  # Map 1D index to 2D
            
#             if mid_value == target:
#                 return True
#             elif mid_value < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
        
#         return False

class Solution:
    def binarysearch(self, l, r, matrix: List[int], target: int) -> bool:
        if l>r:
            return False
        m = l + (r-l)//2
        if matrix[m] == target:
            return True
        elif matrix[m]< target:
            return self.binarysearch(m+1,r, matrix, target)
        return self.binarysearch(l,m-1, matrix, target)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                return self.binarysearch(0, len(matrix[i]) - 1, matrix[i], target)
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))