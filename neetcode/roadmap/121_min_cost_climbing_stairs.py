class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost.append(0)

        for i in range(len(cost)-3, -1, -1):    # start from last before ele (15) in (10,15,20,0)
            cost[i] = min(cost[i]+cost[i+1], cost[i]+cost[i+2])
            # cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])