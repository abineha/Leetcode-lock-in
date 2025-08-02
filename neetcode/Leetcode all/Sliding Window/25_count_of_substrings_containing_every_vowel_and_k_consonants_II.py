from collections import defaultdict

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atleast(k):
            vowel = defaultdict(int)
            l, result, const = 0, 0, 0
            
            for r in range(len(word)):
                if word[r] in 'aeiou':
                    vowel[word[r]] += 1
                else:
                    const += 1
                
                while len(vowel) == 5 and const >= k:
                    result += (len(word) - r)
                    if word[l] in 'aeiou':
                        vowel[word[l]] -= 1
                    else:
                        const -= 1
                    if vowel[word[l]] == 0:
                        vowel.pop(word[l])
                    l += 1
            
            return result

        return atleast(k) - atleast(k+1)