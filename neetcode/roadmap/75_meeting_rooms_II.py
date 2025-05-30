# Given an array of meeting time interval objects consisting of start and end times 
# [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number 
# of days required to schedule all meetings without any conflicts.

# Example 1:

# Input: intervals = [(0,40),(5,10),(15,20)]

# Output: 2
# Explanation:
# day1: (0,40)
# day2: (5,10),(15,20)

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        start = sorted([ i.start for i in intervals])
        end = sorted([ i.end for i in intervals])

        result, count = 0, 0
        s, e = 0, 0     # 2 pointers for start[] end[]

        while s< len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1  # 1 additional meeting goin
            else:
                e += 1      # meeting ober
                count -= 1
            
            result = max(result, count)

        return result