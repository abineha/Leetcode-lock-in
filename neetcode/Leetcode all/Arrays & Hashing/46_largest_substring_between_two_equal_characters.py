class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        map = {}
        result = -1

        for i, c in enumerate(s):
            if map.get(c, -1) == -1:
                map[c] = i
            else:
                result = max(result, i - map[c] - 1)

        return result