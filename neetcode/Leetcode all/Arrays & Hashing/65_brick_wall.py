class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        gap = {0:0}

        for r in wall:
            position = 0
            for brick in r[:-1]:
                position += brick
                gap[position] = 1 + gap.get(position, 0)
        
        return len(wall) - max(gap.values())