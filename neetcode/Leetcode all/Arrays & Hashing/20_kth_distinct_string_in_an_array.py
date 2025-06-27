class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        map = {}
         
        for s in arr:
            map[s] = map.get(s, 0) + 1
        
        for s in arr:
            if map[s] == 1:
                k -= 1
                if k == 0:
                    return s
        return ""
        