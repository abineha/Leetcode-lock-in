class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        map = {}

        for w in words:
            for c in w:
                map[c] = map.get(c, 0) + 1

        for c in map:
            if map[c] % len(words):
                return False

        return True