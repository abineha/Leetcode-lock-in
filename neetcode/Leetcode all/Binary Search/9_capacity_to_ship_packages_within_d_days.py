class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def shippable(cap):
            ship, cur_cap = 1, cap

            for w in weights:
                if cur_cap - w < 0:
                    cur_cap = cap   # recent cap
                    ship += 1   # add new ship with full cap
                cur_cap -= w
            
            return ship <= days
        
        l, r = max(weights), sum(weights)
        result = r

        while l <= r:
            m = (l+r) // 2
            if shippable(m):
                result = min(result, m)
                r = m-1
            else:
                l = m+1
        
        return result