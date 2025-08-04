class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        result = [p for p in prices]
        stack = []

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop()
                result[j] -= prices[i]
            stack.append(i)
        
        return result