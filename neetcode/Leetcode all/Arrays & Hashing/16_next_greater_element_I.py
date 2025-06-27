
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        map = { n:i for i, n in enumerate(nums1)}
        result = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = map[val]
                result[idx] = cur
            if cur in map:
                stack.append(cur)
        return result