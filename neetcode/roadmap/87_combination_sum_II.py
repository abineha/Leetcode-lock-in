class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()   # to avoid [1,7] n [7,1] duplicates

        def dfs(i, cur, total):
            if total == target:
                result.append(cur.copy())
                return
            if total > target or i == len(candidates):
                return
            
            # INCLUDE BRANCH
            cur.append(candidates[i])
            dfs(i+1, cur, total + candidates[i])

            # DOESNT INCLUDE BRANCH
            cur.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)
        return result