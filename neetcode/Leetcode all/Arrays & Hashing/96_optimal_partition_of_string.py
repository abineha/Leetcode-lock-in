class Solution:
    def partitionString(self, s: str) -> int:
        hash = set()
        result = 1

        for c in s:
            if c in hash:
                result += 1
                hash = set()
            hash.add(c)

        return result