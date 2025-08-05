class Solution:
    def removeStars(self, s: str) -> str:
        result = []

        for ele in s:
            if ele == "*" and result:
                    result.pop()
            else:
                result.append(ele)
        
        return "".join(result)