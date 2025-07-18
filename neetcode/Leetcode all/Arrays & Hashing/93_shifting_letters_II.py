# TLE

class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        s = [ord(c)-ord("a") for c in s]

        for l, r, d in shifts:
            for i in range(l, r+1):
                s[i] += 1 if d else -1
                s[i] = s[i] % 26
        
        s = [chr(ord("a")+n) for n in s]
        return "".join(s)
    
# optimized
class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        prefix_dif = [0]*(len(s)+1)

        for l, r, d in shifts:
            prefix_dif[r+1] +=1 if d else -1
            prefix_dif[l] += -1 if d else 1
        
        result = [ord(c)-ord('a') for c in s]
        dif = 0

        for i in reversed(range(len(prefix_dif))):
            dif += prefix_dif[i]
            result[i-1] = (dif+result[i-1]) % 26

        s = [chr(ord('a')+n) for n in result]
        return "".join(s)