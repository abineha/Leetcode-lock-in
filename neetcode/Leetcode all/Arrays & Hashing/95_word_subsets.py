from collections import defaultdict, Counter

class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        map2 = defaultdict(int)

        for w in words2:
            count_w = Counter(w)
            for char, cnt in count_w.items():
                map2[char] = max(map2[char], cnt)
        
        result = []

        for w in words1:
            count_w = Counter(w)
            flag = True
            for char, cnt in map2.items():
                if count_w[char] < cnt:
                    flag = False
                    break
            if flag:
                result.append(w)
        
        return result