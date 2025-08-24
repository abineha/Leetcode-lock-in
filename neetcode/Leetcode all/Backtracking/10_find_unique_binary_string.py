from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        str_set = {s for s in nums}
        
        def back(i, cur):
            if i == len(nums):
                result = "".join(cur)
                return None if result in str_set else result

            result = back(i+1, cur)

            if result:
                return result
            
            cur[i] = "1"

            result = back(i+1, cur)

            if result:
                return result
            
        
        return back(0, ["0" for n in nums])