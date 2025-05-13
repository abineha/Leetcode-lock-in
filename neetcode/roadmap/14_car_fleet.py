class Solution(object):
    def carFleet(self, target, position, speed):
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))