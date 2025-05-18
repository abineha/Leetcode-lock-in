# O(26n)
# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         res = 0
#         charSet = set(s)

#         for c in charSet:
#             count = l = 0
#             for r in range(len(s)):
#                 if s[r] == c:
#                     count += 1

#                 while (r - l + 1) - count > k:
#                     if s[l] == c:
#                         count -= 1
#                     l += 1
                    
#                 res = max(res, r - l + 1)
#         return res

# O (n)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.characterReplacement(s = "ABAB", k = 2))