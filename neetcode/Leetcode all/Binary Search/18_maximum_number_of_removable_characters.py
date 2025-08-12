class Solution:
    def maximumRemovals(self, s: str, p: str, removable: list[int]) -> int:
        def check(s, sub):
            i, j = 0, 0

            while i < len(s) and j < len(sub):
                if i in removed or s[i] != sub[j]:
                    i += 1
                    continue
                i += 1
                j += 1
            
            return j == len(sub)
            
        l, r = 0, len(removable)-1
        result = 0

        while l <= r:
            m = (l+r) // 2
            removed = set(removable[:m+1])

            if check(s, p):
                result = max(result, m+1)
                l = m+1
            else:
                r = m-1
        
        return result