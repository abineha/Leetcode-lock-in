from collections import Counter

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = set()
        L = set()
        R = Counter(s)

        for i in range(len(s)):
            R[s[i]] -= 1
            
            if R[s[i]] == 0:
                R.pop(s[i])
            
            for j in range(26):
                c = chr(ord('a')+j)

                if c in L and c in R:
                    result.add((s[i], c))
            
            L.add(s[i])
        
        return len(result)
        