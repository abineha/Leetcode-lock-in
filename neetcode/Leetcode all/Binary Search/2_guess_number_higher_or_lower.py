# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

def guess(num: int) -> int:
    return 0  # This is a placeholder. The actual implementation will be provided by the system.

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        
        while l <= r:
            m = (l+r) // 2
            gus = guess(m)
            if gus == -1:
                r = m-1
            elif gus == 0:
                return m
            else:
                l = m+1
