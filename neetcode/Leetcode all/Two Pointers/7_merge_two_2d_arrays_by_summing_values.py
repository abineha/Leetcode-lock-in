class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        p1, p2 = 0, 0
        result = []

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1][0] == nums2[p2][0]:
                result.append([nums1[p1][0], nums1[p1][1]+nums2[p2][1]])
                p1, p2 = p1+1, p2+1
            elif nums1[p1][0] > nums2[p2][0]:
                result.append(nums2[p2])
                p2 += 1
            else:
                result.append(nums1[p1])
                p1 += 1
        
        return result + nums1[p1:] + nums2[p2:]