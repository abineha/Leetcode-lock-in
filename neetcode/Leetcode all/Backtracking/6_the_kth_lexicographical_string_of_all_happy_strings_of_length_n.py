class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3*(2**(n-1))
        
        if total < k:
            return ""
        
        result = []
        choice = "abc"
        L, R = 1, total

        for i in range(n):
            cur = L
            part_size = (R-L+1) // len(choice)

            for c in choice:
                if k in range(cur, cur+part_size):
                    result.append(c)
                    L = cur
                    R = cur + part_size - 1
                    choice = "abc".replace(c,"")
                    break
                
                cur += part_size
            
        return "".join(result)