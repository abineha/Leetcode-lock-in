from collections import defaultdict

class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        good_pair = 0
        total_pair = 0
        count = defaultdict(int)
        
        for i in range(len(nums)):
            total_pair += i
            good_pair += count[nums[i]-i]
            count[nums[i]-i] += 1
        
        return total_pair - good_pair
    
# j - i == nums[j] - nums[i]
# --> nums[j] - j == nums[i] - i
# if for some earlier j, 
# we find that nums[j] - j == nums[i] - i, then (j, i) is a good pair.
# for each index i, count[nums[i] - i] tells us how many earlier
# indices j have the same nums[j] - j. We add that to good_pair.