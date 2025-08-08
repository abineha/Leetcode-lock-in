class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        map = {n:i for i, n in enumerate(positions)}
        positions.sort()
        stack = []

        for n in positions:
            i = map[n]
            
            if directions[i] == "R":
                stack.append(i)
            else:
                while stack and (directions[stack[-1]]=="R") and healths[i]:
                    j = stack.pop()
                    if healths[i] > healths[j]:
                        healths[j] = 0
                        healths[i] -= 1
                    elif healths[i] < healths[j]:
                        healths[i] = 0
                        healths[j] -= 1
                        stack.append(j)
                    else:
                        healths[i] = healths[j] = 0

                if healths[i]:
                    stack.append(i)

        return [i for i in healths if i > 0]  