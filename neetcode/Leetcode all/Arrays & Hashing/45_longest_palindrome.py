class Solution:
    def longestPalindrome(self, s: str) -> int:
        map = {}
        result = 0

        for c in s:
            map[c] = map.get(c, 0) + 1
            if map[c] % 2 == 0:
                result +=2

        for c in map.values():
            if c%2 == 1:
                return result + 1

        return result

class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        res = 0

        for c in s:
            if c in seen:
                seen.remove(c)
                res += 2
            else:
                seen.add(c)

        return res + 1 if seen else res