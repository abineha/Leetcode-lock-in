from collections import Counter
from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        char_set = set()

        def overlap(char_set, s):
            total = Counter(char_set) + Counter(s)
            return max(total.values()) > 1
        
        def backtrack(i):
            if i == len(arr):
                return len(char_set)

            result = 0

            if not overlap(char_set, arr[i]):
                for c in arr[i]:
                    char_set.add(c)

                result = backtrack(i+1)

                for c in arr[i]:
                    char_set.remove(c)
            
            return max(result, backtrack(i+1))
        
        return backtrack(0)