class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        result = [0] * len(boxes)
        balls, moves = 0, 0

        for i in range(len(boxes)):
            result[i] = balls + moves
            moves = balls + moves
            balls += int(boxes[i])
        
        balls, moves = 0, 0
        for i in range(len(boxes)-1, -1, -1):
            result[i] += balls + moves
            moves = balls + moves
            balls += int(boxes[i])
        
        return result