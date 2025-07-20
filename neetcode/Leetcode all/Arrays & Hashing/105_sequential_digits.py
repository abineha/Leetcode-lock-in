from collections import deque

class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        result = []
        q = deque(range(1, 10))

        while q:
            n = q.popleft()
            if n > high:
                continue
            if low <= n <= high:
                result.append(n)
            ones = n % 10
            if ones < 9 :
                q.append(n*10+(ones+1))
        
        return result
    
class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        low_dig, high_dig = len(str(low)), len(str(high))
        result = []
        
        for digit in range(low_dig, high_dig+1):
            for start in range(1, 9):
                if start+digit > 10:
                    break
                num = start
                prev = start

                for i in range(digit-1):
                    num = num *10
                    prev += 1
                    num += prev
                
                if low <= num <= high:
                    result.append(num)
        
        return result