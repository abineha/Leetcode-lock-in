class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        l = 0

        for r in range(len(s)):
            if s[r] == " " or r == len(s)-1: 
                p1, p2 = l, r-1 if s[r] == " " else r
                while p1 < p2:
                    s[p1], s[p2] = s[p2], s[p1]
                    p1, p2 = p1+1, p2-1
                l = r+1

        return "".join(s)