class UndergroundSystem:

    def __init__(self):
        self.map = {}   # id -> (start_station, time)
        self.total = {} # (start, end) -> [total_time, count]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.map[id] = (stationName, t)
        

    def checkOut(self, id: int, end_station: str, t: int) -> None:
        start_station, time = self.map[id]
        route = (start_station, end_station)
        if route not in self.total:
            self.total[route] = [0, 0]
        self.total[route][0] += t - time
        self.total[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.total[(startStation, endStation)]
        return total/count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)s