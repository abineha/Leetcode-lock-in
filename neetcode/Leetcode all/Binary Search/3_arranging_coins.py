class Solution:
    def arrangeCoins(self, n: int) -> int:
        ele = 1
        row = 0
        
        while n:
            if n < ele:
                return row
            else:
                n -= ele
                row += 1
                ele += 1

        return row
    
class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        result = 0

        while l <= r:
            m = (l+r) // 2  # m rows
            coins = (m/2) * (1+m)   # coins needed for m rows
            if n < coins:   # m rows too much, not enough coins
                r = m-1     # reduce m rows by reducing r limit
            else:           # m rows sufficiently filled try higher
                l = m+1     # increase left limit to see if more rows can be filled
                result = max(result, m)   # maximise result as m rows can be filled

        return result