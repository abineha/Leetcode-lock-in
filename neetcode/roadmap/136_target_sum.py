from collections import defaultdict

# class Solution:
#     def findTargetSumWays(self, nums: list[int], target: int) -> int:
#         dp = {}     # (index, cur_sum) -> no. of ways
#         # O(n x sum(nums))
        
#         def backtrack(i, cur_sum):
#             if (i, cur_sum) in dp:
#                 return dp[(i, cur_sum)]
#             if i == len(nums):      # end of array
#                 return 1 if cur_sum == target else 0
            
#             dp[(i, cur_sum)] = (backtrack(i+1, cur_sum + nums[i]) + backtrack(i+1, cur_sum - nums[i]))

#             return dp[(i, cur_sum)]
        
#         return backtrack(0, 0)

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
      dp = defaultdict(int)
      dp[0] = 1     # (0 sum) -> 1 way to sum to zero with 1st 0 eles

      for i in range(len(nums)):
        next_dp = defaultdict(int)
        for cur_sum, count in dp.items():
            next_dp[cur_sum + nums[i]] += count
            next_dp[cur_sum - nums[i]] += count
        dp = next_dp
      
      return dp[target]