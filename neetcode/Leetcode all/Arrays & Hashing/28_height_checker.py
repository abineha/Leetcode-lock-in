class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        bucket = [0] * 101

        for h in heights:
            bucket[h] += 1
        
        expected = []

        for h in range(1, 101):
            c = bucket[h]
            for _ in range(c):
                expected.append(h)

        result = 0

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                result += 1

        return result  