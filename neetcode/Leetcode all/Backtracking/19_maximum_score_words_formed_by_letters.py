from collections import Counter
from typing import List

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def can_form_word(w, letter_count):
            word_count = Counter(w)

            for c in word_count:
                if word_count[c] > letter_count[c]:
                    return False
            return True
        
        def get_score(w):
            result = 0 

            for c in w:
                result += score[ord(c) - ord('a')]
            return result

        letter_count = Counter(letters)

        def backtrack(i):
            if i == len(words):
                return 0
            
            # skip
            result = backtrack(i+1)
            # include if possible
            if can_form_word(words[i], letter_count):
                for c in words[i]:
                    letter_count[c] -= 1
                
                result = max(result, get_score(words[i])+backtrack(i+1))

                for c in words[i]:
                    letter_count[c] += 1
            
            return result
        return backtrack(0)