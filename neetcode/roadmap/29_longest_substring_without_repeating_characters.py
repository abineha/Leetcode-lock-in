class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        result = 0
        char_set = set()

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l+=1
            char_set.add(s[r])
            result = max(result, r - l + 1)
        return result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s = "abcabcbb"))