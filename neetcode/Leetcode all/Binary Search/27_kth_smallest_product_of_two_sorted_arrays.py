import bisect
import math

class Solution:
    def kthSmallestProduct(self, nums1: list[int], nums2: list[int], k: int) -> int:
        def count(prod):
            cnt = 0
            n2 = len(nums2)
            for a in nums1:
                if a > 0:
                    cnt += bisect.bisect_right(nums2, prod // a)
                elif a < 0:
                    threshold = math.ceil(prod / a)
                    idx = bisect.bisect_left(nums2, threshold)
                    cnt += n2 - idx
                else:
                    if prod >= 0:
                        cnt += n2
            return cnt


        l, r = -(10**10), 10**10
        while l <= r:
            m = l + (r - l) // 2
            if count(m) < k:
                l = m + 1
            else:
                r = m - 1
        return l