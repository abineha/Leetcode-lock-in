class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        i = 1
        result = 0

        while i < len(neededTime):
            if colors[i] == colors[i-1]:
                if neededTime[i] < neededTime[i-1]:
                    result += neededTime[i]
                    neededTime[i] = neededTime[i-1]
                else:
                    result += neededTime[i-1]
            i += 1

        return result