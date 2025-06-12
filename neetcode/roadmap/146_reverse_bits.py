class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):
            bit = (n >> i) & 1
            result = result | (bit << (31-i))   # 31- i to reverse it left to right, MSB -> LSB
        
        return result