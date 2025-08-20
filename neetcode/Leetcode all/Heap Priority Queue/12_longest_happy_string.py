import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = ""
        q = []

        for f, ch in [(-a, "a"), (-b, 'b'), (-c, 'c')]:
            if f != 0:
                heapq.heappush(q, (f, ch))
        
        while q:
            f, c = heapq.heappop(q)

            if len(result) > 1 and result[-1] == result[-2] == c:   # aaa, bbb, ccc
                if not q:   # no other letter 
                    break
                
                f2, c2 = heapq.heappop(q)   # next best char
                result += c2
                f2 += 1

                if f2:
                    heapq.heappush(q, (f2, c2))
                
                heapq.heappush(q, (f, c))
            
            else:
                result += c
                f += 1

                if f:
                    heapq.heappush(q, (f, c))

        return result