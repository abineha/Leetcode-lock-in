class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        items.sort()
        queries = [(q, i) for i, q in enumerate(queries)]
        queries.sort()
        max_b, j = 0, 0
        result = [0] * len(queries)

        for q, i in queries:
            while j < len(items) and items[j][0] <= q:
                max_b = max(max_b, items[j][1])
                j += 1
            result[i] = max_b

        return result