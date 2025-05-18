# O(M x N)
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         count1 = {}
#         for c in s1:
#             count1[c] = 1 + count1.get(c, 0)
        
#         need = len(count1)
#         for i in range(len(s2)):
#             count2, cur = {}, 0
#             for j in range(i, len(s2)):
#                 count2[s2[j]] = 1 + count2.get(s2[j], 0)
#                 if count1.get(s2[j], 0) < count2[s2[j]]:
#                     break
#                 if count1.get(s2[j], 0) == count2[s2[j]]:
#                     cur += 1
#                 if cur == need:
#                     return True
#         return False
    
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        #  fillin in the letter counts for s1 and the first window in s2
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        # how many letters match exactly
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        # Slide the window along s2
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            # made a match or broke one
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            
            # Remove the old letter (left side)
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            # slide the window
            l += 1
        return matches == 26
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.checkInclusion(s1 = "ab", s2 = "eidbaooo"))