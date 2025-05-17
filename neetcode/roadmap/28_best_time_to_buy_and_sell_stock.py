class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1
        profit = 0

        while r < len(prices):
            if (prices[l] > prices[r]):
                l=r
            else:
                p = prices[r] - prices[l]
                profit = max(profit, p)
            r+=1
        return profit
        
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit(prices = [7,1,5,3,6,4]))