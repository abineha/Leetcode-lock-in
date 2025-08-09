class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num

        while l <= r:
            m = (l+r) // 2
            if m*m < num:
                l = m+1
            elif m*m == num:
                return True
            else:
                r = m-1
        
        return False
            
