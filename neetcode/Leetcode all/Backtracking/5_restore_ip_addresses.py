from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        if len(s) > 12:
            return result

        def back(i, dot, cur):
            if dot == 4 and i == len(s):
                result.append(cur[:-1])
                return
            
            if dot > 4:
                return 

            for j in range(i, min(i+3, len(s))):

                if i != j and s[i] == "0":
                    continue
                
                if int(s[i:j+1]) < 256:
                    back(j+1, dot+1, cur + s[i:j+1] + ".")
        
        back(0, 0, "")
        return result