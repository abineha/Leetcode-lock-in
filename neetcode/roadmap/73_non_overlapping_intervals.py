class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # sort da intervals array
        intervals.sort()    # default based on 1st index
        result = 0 
        prevEnd = intervals[0][1]   # track of prev end added to result
        
        for start, end in intervals[1:]: 
            # not overlapping
            if start >= prevEnd:
                prevEnd = end
            # overlapping
            else:
                result += 1
                prevEnd = min(prevEnd, end)

        return result