class Solution:
    def myPow(self, x: float, n: int) -> float:
        def nsqr(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            result = nsqr(x, n//2)
            result = result*result
            
            return x * result if n%2 else result
        
        result = nsqr(x, abs(n))
        return result if n >= 0 else 1/result