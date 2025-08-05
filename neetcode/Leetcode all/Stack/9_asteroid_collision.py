class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                if abs(a) == stack[-1]:
                    stack.pop()
                    break
                elif abs(a) > stack[-1]:
                    stack.pop()
                else:
                    break
            else:   # if while didnt encounter break
                stack.append(a)

        return stack
