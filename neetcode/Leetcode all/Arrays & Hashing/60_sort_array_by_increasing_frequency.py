from collections import Counter

class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        count = Counter(nums)
        nums.sort(key = lambda n : (count[n], -n))
        return nums