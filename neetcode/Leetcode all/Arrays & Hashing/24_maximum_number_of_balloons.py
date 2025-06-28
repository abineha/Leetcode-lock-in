from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        map = defaultdict(int)
        for c in text:
            if c in "balloon":
                map[c] += 1

        if len(map) < 5:
            return 0
        
        map['l'] //= 2
        map["o"] //= 2

        return min(map.values())

        