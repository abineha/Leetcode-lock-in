from collections import Counter

class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        total = sum(skill)

        if total %(len(skill)//2):
            return -1

        map = Counter(skill)
        result = 0
        target = total // (len(skill)//2)

        for s in skill:
            if not map[s]:  # count = 0
                continue
            
            map[s] -= 1   # use up s
            diff = target - s
            
            if not map[diff]: # count of diff = 0
                return -1
            
            result += s*diff
            map[diff] -= 1    # use up diff
        
        return result