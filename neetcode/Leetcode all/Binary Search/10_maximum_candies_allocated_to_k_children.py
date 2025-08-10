class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        elif sum(candies) == k:
            return 1
        else:
            l, r = 1, max(candies)
            result = 0 

            while l <= r:
                m = (l+r) // 2  # number of candies for each child = each pile size
                total_children = sum(pile // m for pile in candies) 

                if total_children >= k:
                    result = max(result, m)
                    l = m+1
                else:
                    r = m-1
            
            return result