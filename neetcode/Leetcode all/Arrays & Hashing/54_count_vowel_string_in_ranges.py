class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        prefix = [0] * (len(words) + 1)
        prev = 0
        vowel = set("aeiou")

        for i, v in enumerate(words):
            if v[0] in vowel and v[-1] in vowel:
                prev += 1
            prefix[i+1] = prev

        result = []
        for q in queries:
            l, r = q
            result.append(prefix[r+1] - prefix[l])

        return result