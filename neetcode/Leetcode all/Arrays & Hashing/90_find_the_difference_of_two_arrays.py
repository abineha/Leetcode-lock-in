class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1, set2 = set(nums1), set(nums2)
        r1, r2 = [], []

        for n in set1:
            if n not in set2:
                r1.append(n)
        for n in set2:
            if n not in set1:
                r2.append(n)
        
        return [r1, r2]