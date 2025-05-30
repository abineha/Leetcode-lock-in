class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # sort intervals array
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]   # adding 1st interval

        for start, end in intervals[1:]:  # since we already added 1st interval
            lastEnd = output[-1][1]   # last ele's end value in o/p
            if start <=lastEnd:      # overlapping so merge
                output[-1][1] = max(lastEnd, end)

            # [1, 5] [2, 4] -> [1, 5]        
            else:
                output.append([start, end])    
        return output