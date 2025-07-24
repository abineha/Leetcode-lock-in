from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        map = Counter(s)
        odd, even = 0, len(s)

        for n in map.values():
            if n & 1:
                odd = max(odd, n)
            else:
                even = min(even, n)
        
        return (odd-even)