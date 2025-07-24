from collections import defaultdict

class Solution:
    def distinctNames(self, ideas: list[str]) -> int:
        # map first char -> list of word's suffixes
        wordMap = defaultdict(set)
        result = 0

        for w in ideas:
            wordMap[w[0]].add(w[1:])
        
        for char1 in wordMap:   # 26 chars
            for char2 in wordMap:
                if char1 == char2:
                    continue
                intersect = 0

                for w in wordMap[char1]:    # duplicate suffixes
                    if w in wordMap[char2]:
                        intersect += 1
                
                distinct1 = len(wordMap[char1]) - intersect
                distinct2 = len(wordMap[char2]) - intersect
                result += distinct1 * distinct2
        
        return result