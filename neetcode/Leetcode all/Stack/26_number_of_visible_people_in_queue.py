class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        stack = []
        n = len(heights)
        result = [0] * n

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] < h:
                result[stack.pop()] += 1
            
            if stack:
                result[stack[-1]] += 1
            
            stack.append(i)
        
        return result