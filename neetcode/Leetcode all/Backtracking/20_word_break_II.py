from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)

        def backtrack(i):
            if i == len(s):
                result.append(" ".join(cur))
                return 
                
            for j in range(i, len(s)):
                w = s[i:j+1]
                if w in wordDict:
                    cur.append(w)
                    backtrack(j+1)
                    cur.pop()
        
        cur = []
        result = []
        backtrack(0)
        return result