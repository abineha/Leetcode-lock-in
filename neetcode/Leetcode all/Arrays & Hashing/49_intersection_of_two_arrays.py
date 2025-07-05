class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        res = []
        for num in set1:
            if num in set2:
                res.append(num)
        return res
    
# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         seen = defaultdict(int)
#         for num in nums1:
#             seen[num] = 1
        
#         res = []
#         for num in nums2:
#             if seen[num] == 1:
#                 seen[num] = 0
#                 res.append(num)
#         return res