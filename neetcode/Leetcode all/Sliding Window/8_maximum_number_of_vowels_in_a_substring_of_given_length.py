class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l, result, total = 0, 0, 0
        vowel = set(['a','e','i','o','u'])

        for r in range(len(s)):
            total += 1 if s[r] in vowel else 0
            if (r-l+1) > k:
                total -= 1 if s[l] in vowel else 0
                l += 1
            result = max(result, total)
        
        return result