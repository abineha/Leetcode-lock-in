from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        l = sum(matchsticks) // 4
        side = [0] * 4

        if sum(matchsticks) /4 != l:
            return False

        matchsticks.sort(reverse = True)

        def back(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if side[j] + matchsticks[i] <= l:
                    side[j] += matchsticks[i]

                    if back(i+1):
                        return True
                    
                    side[j] -= matchsticks[i]
            
            return False
        
        return back(0)