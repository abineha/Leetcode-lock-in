class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)    # 0...amount
        dp[0] = 0   # 0 coins -> sum = 0

        for a in range(amount+1):
            for c in coins:
                if (a-c) >= 0:  # get amount = a
                    dp[a] = min(dp[a], 1 + dp[a-c])        
        
        return  dp[amount] if dp[amount] != (amount+1) else -1