class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s+s
        tar1, tar2 = "", ""

        for i in range(len(s)):
            tar1 += "0" if i%2 else "1"
            tar2 += "1" if i%2 else "0"

        result = len(s)
        dif1, dif2, l = 0, 0, 0

        for r in range(len(s)):
            if s[r] != tar1[r]:
                dif1 += 1
            if s[r] != tar2[r]:
                dif2 += 1
            if (r-l+1) > n:
                if s[l] != tar1[l]:
                    dif1 -= 1
                if s[l] != tar2[l]:
                    dif2 -= 1
                l += 1
            if (r-l+1) == n:
                result = min(result, dif1, dif2)
        
        return result