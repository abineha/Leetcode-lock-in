from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        map = Counter(tiles)

        def dfs():
            result = 0
            for c in map:
                if map[c] > 0:
                    map[c] -= 1
                    result += 1     # forms a valid sequence

                    result += dfs()     # go further

                    map[c] += 1     # undo the choice
            
            return result
        
        return dfs()