# BRUTE FORCE = TLE
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def is_pali(s, l ,r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l, r = l+1, r-1
            return True
        
        for r in reversed(range(len(s))):
            if is_pali(s, 0, r):
                suffix = s[r+1:]
                return suffix[::-1]+s
            
        return ""
    
# OPTIMAL = Rabin Karp
# This builds the forward rolling hash:

# prefix as building up `s[0..i]` using polynomial hashing: 

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        prefix = 0
        sufix = 0
        base = 29
        last_idx = 0
        power = 1
        mod = 10**9 + 7

        for i, c in enumerate(s):
            char = (ord(c)-ord('a')+1)
            prefix = (prefix*base) % mod
            prefix = (prefix+char) % mod
            sufix = (sufix+char*power) % mod
            power = (power*base) % mod

            if prefix == sufix:
                last_idx = i
        
        sufix = s[last_idx+1:]
        return sufix[::-1]+s