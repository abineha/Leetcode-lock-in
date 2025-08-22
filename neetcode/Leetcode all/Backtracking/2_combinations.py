from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(start, li):
            if len(li) == k:
                result.append(li.copy())
                return 
            
            for i in range(start, n+1):
                li.append(i)
                backtrack(i+1, li)
                li.pop()
        
        backtrack(1, [])
        return result