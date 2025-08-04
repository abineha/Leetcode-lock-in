class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stak = []
        result = 0

        for ele in operations:
            if ele == '+':
                if len(stak) >= 2:
                    stak.append(int(stak[-1])+int(stak[-2]))
                    result += stak[-1]
            elif ele == 'D':
                if stak:
                    stak.append(2*stak[-1])
                    result += stak[-1]
            elif ele == 'C':
                if stak:
                    result -= stak.pop()
            else:
                stak.append(int(ele))
                result += stak[-1]

        return sum(stak)