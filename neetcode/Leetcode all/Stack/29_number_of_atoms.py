from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [ defaultdict(int) ]
        i, n = 0, len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                i += 1
                start = i

                while i < n and formula[i].isdigit():
                    i += 1
                
                mult = int(formula[start:i] or 1)
                top = stack.pop()
                
                for atom, count in top.items():
                    stack[-1][atom] += count * mult
            else:
                start = i
                i += 1
                
                while i < n and formula[i].islower():
                    i += 1
                
                atom = formula[start:i]
                start = i

                while i < n and formula[i].isdigit():
                    i += 1
                
                num = int(formula[start:i] or 1)
                stack[-1][atom] += num
        
        result = ""
        
        for atom in sorted(stack[0]):
            result += atom + (str(stack[0][atom]) if stack[0][atom] > 1 else '')
        
        return result