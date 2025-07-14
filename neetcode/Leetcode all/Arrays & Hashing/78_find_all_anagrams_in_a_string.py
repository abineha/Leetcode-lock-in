class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s) < len(p):
            return []

        p_map, s_map = {}, {}
        
        for i in range(len(p)):
            p_map[p[i]] = 1 + p_map.get(p[i], 0)
            s_map[s[i]] = 1 + s_map.get(s[i], 0)

        result = [0] if p_map == s_map else []
        l = 0

        for r in range(len(p), len(s)):
            s_map[s[r]] = 1 + s_map.get(s[r], 0)
            s_map[s[l]] -= 1
            if s_map[s[l]] == 0:
                s_map.pop(s[l])
            l += 1
            if s_map == p_map:
                result.append(l)
        
        return result
 