from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operations = { "+" : lambda x, y: x+y,
                       "-" : lambda x, y: x-y,
                       "*" : lambda x, y: x*y } 
        
        def backtrack(L, R):
            result = []

            for i in range(L, R+1):
                op = expression[i]
                
                if op in operations:
                    nums1 = backtrack(L, i-1)
                    nums2 = backtrack(i+1, R)
                
                    for n1 in nums1:
                        for n2 in nums2:
                            result.append(operations[op](n1, n2))
            
            if result == []:
                result.append(int(expression[L:R+1]))
            
            return result
        
        return backtrack(0, len(expression)-1)