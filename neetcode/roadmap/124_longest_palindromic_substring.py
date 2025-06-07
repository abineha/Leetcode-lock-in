class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        reslen = 0

        def expandAroundCenter(left: int, right: int):
            nonlocal result, reslen
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > reslen:
                    reslen = right - left + 1
                    result = s[left:right+1]
                left -= 1
                right += 1

        for i in range(len(s)):
            expandAroundCenter(i, i)     # odd-length palindrome
            expandAroundCenter(i, i+1)   # even-length palindrome

        return result
