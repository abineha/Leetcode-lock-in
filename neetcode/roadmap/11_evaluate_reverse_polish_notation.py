class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack=[]
        for c in tokens:
            if c=="+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif c=="-": 
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(b - a)
            elif c=="*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif c=="/":
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[0]

if __name__ == "__main__":
    sol = Solution()
    print(sol.evalRPN(tokens = ["2","1","+","3","*"]))