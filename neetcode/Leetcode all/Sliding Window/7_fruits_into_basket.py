from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        map = defaultdict(int)
        l, result, total = 0, 0, 0

        for r in range(len(fruits)):
            map[fruits[r]] += 1
            total += 1

            while len(map) > 2:
                f = fruits[l]
                map[f] -= 1
                total -= 1
                l += 1
                if not map[f]:
                    map.pop(f)

            result = max(result, total)

        return result