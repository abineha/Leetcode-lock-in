class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")]*n
        prices[src] = 0

        for i in range(k+1):
            tempPrices = prices.copy()

            for s, d, p in flights:
                if prices[s] == float("inf"):   # cant reach this node - inf
                    continue
                if prices[s] + p < tempPrices[d]:
                    tempPrices[d] = prices[s] + p
            prices = tempPrices
        
        return -1 if prices[dst] == float("inf") else prices[dst]