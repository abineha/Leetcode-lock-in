
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:    # end val < start val
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > intervals[i][1]:   # start val > end val
                result.append(intervals[i])
            else: # overlapping
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        result.append(newInterval)
        return result