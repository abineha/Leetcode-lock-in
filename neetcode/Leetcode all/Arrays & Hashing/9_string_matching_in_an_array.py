class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        result = []
        # n^2 l^2

        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:  # same word
                    continue

                if words[i] in words[j]:
                    result.append(words[i])
                    break
        return result    