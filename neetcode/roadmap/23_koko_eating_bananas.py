import math
# BRUTE FOR
# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         speed = 1
#         while True:
#             totalTime = 0
#             for pile in piles:
#                 totalTime += math.ceil(pile / speed)
            
#             if totalTime <= h:
#                 return speed
#             speed += 1
#         return speed

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        speed = r # max of pile (worst case)

        while l <= r: 
            k = (l+r) // 2
            hrs = 0
            for p in piles:
                hrs += math.ceil(p/k)
            
            if hrs <= h:
                speed = min(speed, k)
                r = k - 1 # search for min
            else:
                l = k + 1 # rate too small cant eat within hrs
        return speed

if __name__ == "__main__":
    sol = Solution()
    print(sol.minEatingSpeed(piles = [3,6,7,11], h = 8))