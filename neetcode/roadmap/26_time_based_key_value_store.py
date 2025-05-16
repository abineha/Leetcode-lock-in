class TimeMap:

    def __init__(self):
        self.map = {} # key = "", val = [[v, t]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [] # empty list
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.map.get(key,[])
        # binary search
        l, r = 0, len(values) - 1
        while l <=r :
            m = (l+r)//2
            if values[m][1] <= timestamp:
                result = values[m][0]
                l = m + 1 # search right
            else:
                r = m - 1 # search left 
        return result

