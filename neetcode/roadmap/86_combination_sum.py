class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def dfs(i, cur, total):
            if total == target:
                result.append(cur.copy())
                return
            if target < total or i >= len(candidates):  # out of bounds
                return  
            
            cur.append(candidates[i])   # INCLUDE
            dfs(i, cur, total + candidates[i])

            cur.pop()   # NOT INCLUDE
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return result