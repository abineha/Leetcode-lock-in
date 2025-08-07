from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7  # To avoid overflow and keep result within limits
        result, stack = 0, []  # Stack holds tuples: (index, value)

        # Process each element in the array
        for i, n in enumerate(arr):
            # While current number is less than the top of the stack,
            # we found the end of influence of stack[-1]
            while stack and n < stack[-1][1]:
                j, m = stack.pop()  # m is the number being popped
                # Distance to the previous smaller element
                left = j - stack[-1][0] if stack else (j + 1)
                # Distance to the next smaller element (current index - popped index)
                right = i - j
                # m is the minimum for left * right subarrays
                result = (result + m * left * right) % MOD
            # Push current element onto the stack
            stack.append((i, n))

        # Process remaining elements in the stack
        for i in range(len(stack)):
            j, n = stack[i]
            # Distance to previous smaller element (or to the start)
            left = j - stack[i-1][0] if i > 0 else (j + 1)
            # Distance to the end of array
            right = len(arr) - j
            # n is the minimum for left * right subarrays
            result = (result + n * left * right) % MOD

        return result
