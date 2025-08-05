class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        pop_idx = 0

        for i in pushed:
            stack.append(i)
            while stack and popped[pop_idx] == stack[-1]:
                pop_idx += 1
                stack.pop()

        return len(popped) == pop_idx