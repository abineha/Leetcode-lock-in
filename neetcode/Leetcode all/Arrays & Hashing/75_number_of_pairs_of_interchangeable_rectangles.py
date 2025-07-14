class Solution:
    def interchangeableRectangles(self, rectangles: list[list[int]]) -> int:
        map = {}    # w/h : count

        for w, h in rectangles:
            map[w/h] = map.get(w/h, 0) + 1
        
        result = 0 
        for c in map.values():
            if c > 1 :
                result += (c*(c-1)) // 2
        
        return result