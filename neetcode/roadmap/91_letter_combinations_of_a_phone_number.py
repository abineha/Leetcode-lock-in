class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        result = []
        digits_to_char = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        
        def backtrack(i, curstr):
            if len(curstr) == len(digits):
                result.append(curstr)   # strings are immutable, so no need to copy them.
                return
            
            for c in digits_to_char[digits[i]]:
                backtrack(i+1, curstr + c)
        
        if digits:
            backtrack(0, "")
        return result