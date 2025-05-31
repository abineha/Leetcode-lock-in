class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total, result = 0, 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:   # doesnt work
                total = 0   # reset
                result = i+1  # atleast 1 position def as unique soln exists

        return result