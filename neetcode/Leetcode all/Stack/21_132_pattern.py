class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack = []  # pair [num, minleft], monotonic decreasing
        cur_min = nums[0]

        for n in nums[1:]:
            while stack and n >= stack[-1][0]:
                stack.pop()
            if stack and (n<stack[-1][0]) and n > stack[-1][1]:
                return True
            
            stack.append([n, cur_min])
            cur_min = min(cur_min, n)
        
        return False