# If nums = [a, b, c, d, e], and i = 2 (element c),
# then:
# result[2] = |c - a| + |c - b| + |c - c| + |c - d| + |c - e|
#           = (c-a + c-b) + 0 + (d-c + e-c)
#           = (2 * c - (a + b)) + ((d + e) - 2 * c)

# Left of i (0 to i-1):
# There are i elements. Their sum is left_sum.
# Their absolute diff: i * nums[i] - left_sum

# Right of i (i+1 to n-1):
# There are (n - i - 1) elements. Their sum is right_sum.
# Their absolute diff: right_sum - (n - i - 1) * nums[i]

class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        total = sum(nums)
        left_sum = 0
        result = []

        for i, n in enumerate(nums):
            right_sum = total - left_sum - n
            result.append((i*n)-left_sum + right_sum-(len(nums)-i-1)*n)
            left_sum += n
        
        return result
