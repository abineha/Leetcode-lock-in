from collections import Counter, defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        map = Counter(s)
        bucket = defaultdict(list)
        result = []

        for char, cnt in map.items():
            bucket[cnt].append(char)
        
        for i in range(len(s), -1, -1):
            for c in bucket[i]:
                result.append(c*i)
        
        return "".join(result)