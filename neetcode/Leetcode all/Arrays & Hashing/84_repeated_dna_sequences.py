class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        seen, result =set(), set()

        for l in range(len(s)-9):
            cur = s[l:l+10]
            if cur in seen:
                result.add(cur)
            seen.add(cur)
        
        return list(result)