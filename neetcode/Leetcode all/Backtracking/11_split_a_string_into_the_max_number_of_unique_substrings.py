class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(i, cur_set):
            if i == len(s):
                return 0
            
            result = 0

            for j in range(i, len(s)):
                substr = s[i:j+1]

                if substr in cur_set:
                    continue
                
                cur_set.add(substr)
                result = max(result, 1 + dfs(j+1, cur_set))
                cur_set.remove(substr)
            

            return result
        
        return dfs(0, set())