class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result = []
        open = 0    # extra (
            
        for c in s:
            if c == "(":
                result.append(c)
                open += 1
            elif c == ")" and open>0:
                result.append(')')
                open -= 1
            elif c != ')':
                result.append(c)

        filtered = []

        for c in result[::-1]:
            if c == "(" and open > 0:
                open -=1
            else: 
                filtered.append(c)
        
        return "".join(filtered[::-1])