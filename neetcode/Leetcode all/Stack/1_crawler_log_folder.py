class Solution:
    def minOperations(self, logs: list[str]) -> int:
        stak = []

        for ele in logs:
            if ele == "../":
                if stak:
                    stak.pop()
            elif ele == "./":
                continue
            else:
                stak.append(ele)

        return len(stak)
    
class Solution:
    def minOperations(self, logs: list[str]) -> int:
        ptr = 0  
        for log in logs:
            if log == "../":
                if ptr > 0:
                    ptr -= 1
            elif log == "./":
                continue
            else:
                ptr += 1
        return ptr
