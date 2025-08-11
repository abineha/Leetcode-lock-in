from math import sqrt

class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        def helper(time):
            count = 0
            
            for r in ranks:
                count += int(sqrt(time/r))
            
            return count
        
        l, r = 0, ranks[0]*cars*cars
        result = -1

        while l <= r:
            m = (l+r) // 2
            repair = helper(m)
            
            if repair >= cars:
                result = m
                r = m-1
            else:
                l = m+1
        
        return result