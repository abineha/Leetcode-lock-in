class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        char_word = {}
        word_char = {}

        for c, w in zip(pattern, words):
            if c in char_word and char_word[c] != w:
                return False
            if w in word_char and word_char[w] != c:
                return False
            char_word[c] = w
            word_char[w] = c

        return True       