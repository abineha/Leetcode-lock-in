import math 

class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        def distribute(x):
            stores = 0
            for q in quantities:
                stores += math.ceil(q/x)
            
            return stores <= n 
        
        l, r = 1, max(quantities)
        result = 0
        
        while l <= r:
            m = (l+r) // 2
            if distribute(m):
                r = m-1
                result = m
            else:
                l = m+1
            
        return result