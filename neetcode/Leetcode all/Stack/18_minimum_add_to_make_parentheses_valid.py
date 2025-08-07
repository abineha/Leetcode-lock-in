class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0

        for c in s:
            if c =="(":
                stack.append(c)
            elif stack and c ==")" and stack[-1] =="(":
                stack.pop()
            else:
                count += 1
        
        return len(stack) + count
    
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        o, result = 0, 0

        for c in s:
            if c =="(":
                o += 1
            else:
                o -= 1
                if o < 0:
                    o = 0
                    result += 1
        
        return o + result