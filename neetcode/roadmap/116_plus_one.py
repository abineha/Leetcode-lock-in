class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits = digits[::-1]   # reverse it
        one,i = 1, 0

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(1)
                one = 0
            i += 1

        return digits[::-1]
        