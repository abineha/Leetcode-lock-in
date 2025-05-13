# TLE:
# class Solution(object):
#     def dailyTemperatures(self, temperatures):
#         """
#         :type temperatures: List[int]
#         :rtype: List[int]
#         """
#         l = []
#         while (temperatures):
#             curr = temperatures.pop(0)
#             print(curr)
#             l.append(0)
#             n = 1
#             for i in temperatures:
#                 if (i>curr):
#                     l[-1] = n
#                     break
#                 else: 
#                     n+=1
#                     continue

#         return l
        

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0] * len(temperatures)
        stack = [] # [ i , t]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                si, st = stack.pop()
                result[si] = i - si
            stack.append([i , t])
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))

