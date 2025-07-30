# BRUTE FORCE
class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        N = len(code)
        result = [0] * N

        if k == 0:
            return result
        
        for i in range(N):
            if k > 0:
                for j in range(i+1, i+k+1):
                    result[i] += code[j%N]
            elif k < 0:
                for j in range(i-1, i-abs(k)-1, -1):
                    result[i] += code[j%N]

        return result
    
# SLIDING WINDOW
class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        N = len(code)
        result = [0] * N
        l, total = 0, 0
        
        for r in range(N+abs(k)):
            total += code[r%N]

            if (r-l+1) > abs(k):
                total -= code[l%N]
                l = (l+1) % N
            if (r-l+1) == abs(k):
                if k > 0:
                    result[(l-1)%N] = total
                elif k < 0:
                    result[(r+1)%N] = total

        return result