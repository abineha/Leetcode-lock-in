class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # add ( if o < n
        # add ) if c < o
        # if o = c = n then valid

        stack = [] # global stack
        result = []

        def recursivecall(o,c):
            if o == c == n:
                result.append("".join(stack))
                return
            if o < n:
                stack.append("(")
                recursivecall(o+1,c)
                stack.pop()  # clean global stack
            if c < o:
                stack.append(")")
                recursivecall(o,c+1)
                stack.pop()  # clean global stack
        
        recursivecall(0,0)
        return result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(n = 3))