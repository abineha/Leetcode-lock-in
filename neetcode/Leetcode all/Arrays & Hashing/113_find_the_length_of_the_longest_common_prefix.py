class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1
        
        result = 0
        prefix_set = set()

        for n in arr1:
            while n and n not in prefix_set:
                prefix_set.add(n)
                n = n // 10
        
        for n in arr2:
            while n and n not in prefix_set:
                n = n // 10
            if n :
                result = max(result, len(str(n)))

        return result