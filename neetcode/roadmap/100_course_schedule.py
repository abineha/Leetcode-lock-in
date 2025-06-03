class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        # Map each course to its prerequisites
        hashmap = { i:[] for i in range(numCourses)}
        
        for c, p in prerequisites:
            hashmap[c].append(p)

        # visitSet =  all courses along current DFS path
        visitSet = set()

        def dfs(c):
            if c in visitSet:   # loop / deadlock
                return False
            if hashmap[c] == []:      # no prerequisites 
                return True
            
            visitSet.add(c)

            for p in hashmap[c]:      # all prerequisites for given course
                if not dfs(p):
                    return False
            
            visitSet.remove(c)        # check finished
            hashmap[c] = []           # already checked if finishable
            return True
        
        for c in range(numCourses):   # if graph not connected (1->2) (3->4)
            if not dfs(c):
                return False
        
        return True