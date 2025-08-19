import heapq

class SeatManager:

    def __init__(self, n: int):
        self.q = []
        self.nextSeat = 1

    def reserve(self) -> int:
        if self.q:
            return heapq.heappop(self.q)
        
        seat = self.nextSeat
        self.nextSeat += 1
        return seat        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.q, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)