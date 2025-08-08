class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def eval(expr):
            if expr == 't':
                return True
            if expr == 'f':
                return False

            if expr[0] == '!':
                return not eval(expr[2:-1])

            if expr[0] in '&|':
                parts, cur = [], []
                bal = 0
                for c in expr[2: -1]:
                    if c == ',' and bal ==0:
                        parts.append("".join(cur))
                        cur = []
                    else:
                        if c == '(':
                            bal += 1
                        elif c == ')':
                            bal -= 1
                        cur.append(c)
                
                parts.append("".join(cur))
                
                if expr[0] == "&":
                    return all(eval(p) for p in parts)
                else:
                    return any(eval(p) for p in parts)
        
        return eval(expression)