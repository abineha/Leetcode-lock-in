class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = min(len(word1), len(word2))
        result = ""

        for p in range(l):
            result += word1[p] + word2[p]

        return result + word1[l:] + word2[l:]