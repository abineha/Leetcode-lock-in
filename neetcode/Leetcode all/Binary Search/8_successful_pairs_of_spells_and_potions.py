class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        result = []

        for s in spells:
            l, r = 0, len(potions)-1
            idx = len(potions)

            while l <= r:
                m = (l+r) // 2
                if s * potions[m] >= success:
                    r = m-1
                    idx = m
                else:
                    l = m+1
            
            result.append(len(potions)-idx)

        return result