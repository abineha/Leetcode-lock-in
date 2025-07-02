class Solution:
    def minOperations(self, s: str) -> int:
        count = 0

        for i in range(len(s)): # 01010101....
            if i % 2 == 0 :     # even pos = 0
                count += 1 if s[i] == "0" else 0
            else:               # odd pos = 1
                count += 1 if s[i] == "1" else 0
        
        return min(count, len(s)-count)
        