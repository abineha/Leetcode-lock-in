class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        map = {p[0]:p[1] for p in paths}
        start = paths[0][0]
        
        while start in map:
            start = map[start]
        
        return start
        