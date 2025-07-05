from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        map = Counter(words[0])
        result = []

        for w in words:
            cur_map = Counter(w)
            for c in map:
                map[c] = min(map[c], cur_map[c])

        for c in map:
            for i in range(map[c]):
                result.append(c) 

        return result   