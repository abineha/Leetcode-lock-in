from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        result = [0] * (2*n - 1)
        used = set()

        def backtrack(i):
            if i == len(result):
                return True
            
            for num in reversed(range(1, n+1)):
                if num in used:
                    continue
                if num > 1 and (i+num >= len(result) or result[i+num]):
                    continue
                
                # try decision
                used.add(num)
                result[i] = num
                if num > 1:
                    result[i+num] = num
                
                # next index spot to fill
                j = i+1
                while j < len(result) and result[j]:
                    j += 1
                
                # recursive step
                if backtrack(j):
                    return True
                
                # used to backtrack
                used.remove(num)
                result[i] = 0

                if num > 1:
                    result[i+num] = 0
                
            return False
        
        backtrack(0)
        return result