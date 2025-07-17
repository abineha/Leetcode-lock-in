class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        hash = set()

        for i in range(len(s)-k+1):
            hash.add(s[i:i+k])

        return True if len(hash) == 2**k else False