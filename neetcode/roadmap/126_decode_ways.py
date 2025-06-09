class Solution:
    def numDecodings(self, s: str) -> int:
        dp = { len(s) : 1}  #empty str returns 1
        
        for i in range(len(s)-1, -1, -1):
            if s[i] =="0":  # starts with zero
                dp[i] = 0
            else: 
                dp[i] = dp[i+1]
            
            if (i+1 < len(s) and (s[i] == "1" or s[i]=="2" and s[i+1] in "0123456")): #10-26
                dp[i] += dp[i+2]
            
        return dp[0]
    
        # dp = { len(s) : 1}
        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     if s[i] == "0":
        #         return 0
            
        #     result = dfs(i+1)
        #     if (i+1 < len(s) and (s[i] == "1" or s[i]=="2" and s[i+1] in "0123456")): #10-26
        #         result += dfs(i+2)
        #     dp[i] = result
        #     return result
        # return dfs(0)
