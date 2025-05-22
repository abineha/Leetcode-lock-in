import collections
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output = []
        q = collections.deque()  # index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:  # current bigger than what is at end of q, remove smaller ones
                q.pop()
            q.append(r)  # expand window

            if l > q[0]: # left index out of bounds of slided window
                q.popleft()

            if (r + 1) >= k:    # window full ?
                output.append(nums[q[0]])   # front of q is max
                l += 1  # move left of window
            r += 1  # move right of window

        return output
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))