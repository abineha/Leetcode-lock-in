from collections import defaultdict

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        map = defaultdict(int)

        for n in nums:
            map[n] += 1
            if len(map) <= 2:
                continue
            new_map = defaultdict(int)

            for n, c in map.items():
                if c > 1:   # wont become 0 while decrementing
                    new_map[n] = c - 1
            map = new_map

        result = []
        for n in map:
            if nums.count(n) > len(nums)//3:
                result.append(n)
        
        return result
