class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefix_n = [0]*(n+1)
        postfix_y = [0]*(n+1)

        for i in range(1, n+1):
            prefix_n[i] = prefix_n[i-1]
            if customers[i-1] == 'N':
                prefix_n[i] += 1
        
        for i in range(n-1, -1, -1):
            postfix_y[i] = postfix_y[i+1]
            if customers[i] == "Y":
                postfix_y[i] += 1
        
        min_penalty, idx = float('inf'), 0

        for i in range(n+1):
            penalty = prefix_n[i] + postfix_y[i]
            if penalty < min_penalty:
                min_penalty = penalty
                idx = i
        
        return idx
    
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        if "Y" not in customers:    # best closing time is at the start (0)
            return 0
        if "N" not in customers:    # best closing time is at the very end
            return len(customers)
        
        profit = 0
        maxP = 0
        bestCT = 0

        for i,v in enumerate(customers):
            profit += 1 if v == "Y" else -1 # If customer came ('Y'), add +1 to profit (store stayed open during valuable time)
            # If no customer ('N'), subtract -1 (penalty for staying open unnecessarily).
            if profit > maxP:
                maxP = profit
                bestCT = i + 1  # If this is the best profit so far, update maxP and set bestCT to next hour (i+1). Because closing happens after this hour.
        return bestCT