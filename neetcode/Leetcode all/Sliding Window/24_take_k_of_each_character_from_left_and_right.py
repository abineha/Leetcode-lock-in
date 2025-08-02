class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # total counts
        count = [0, 0, 0]   # a, b, c
        for c in s:
            count[ord(c)-ord('a')] += 1
        if min(count) < k:
            return -1
        
        # sliding window
        result, l = float('inf'), 0
        for r in range(len(s)):
            count[ord(s[r])-ord('a')] -= 1  # window
            while min(count) < k:   # invalid
                count[ord(s[l])-ord('a')] += 1  # put out of window till valid
                l += 1
            result = min(result, len(s)-(r-l+1))    # ans is all out of window
        
        return result