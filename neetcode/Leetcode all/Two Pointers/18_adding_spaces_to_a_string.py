class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        last, result = 0, []

        for i in range(len(spaces)):
            result.append(s[last:spaces[i]])
            result.append(" ")
            last = spaces[i]

        result.append(s[last:])
        return "".join(result) 