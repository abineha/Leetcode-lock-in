class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        count = 0
        map = {}
        for i in allowed:
            map[i] = map.get(i, 0) + 1
        
        for w in words:
            flag = 0
            for i in w:
                if map.get(i, 0) != 0:
                    continue
                else:
                    flag = 1
                    break
            if flag == 0:
                count += 1
        
        return count
        

class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        allowed_set = set(allowed)
        count = 0
        for word in words:
            if all(c in allowed_set for c in word):
                count += 1
        return count