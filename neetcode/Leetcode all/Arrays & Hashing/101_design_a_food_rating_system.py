from sortedcontainers import SortedSet
from collections import defaultdict
class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.map = defaultdict(SortedSet)   # cuisines -> (rating, food)
        self.map_c = {}     # food -> cuisine
        self.map_r = {}     # food -> rating

        for i in range(len(foods)):
            self.map[cuisines[i]].add((-ratings[i], foods[i]))
            self.map_c[foods[i]] = cuisines[i]
            self.map_r[foods[i]] = ratings[i]


    def changeRating(self, food: str, newRating: int) -> None:
        c = self.map_c[food]
        r = self.map_r[food]
        self.map[c].remove((-r, food))
        self.map[c].add((-newRating, food))
        self.map_r[food] = newRating        

    def highestRated(self, cuisine: str) -> str:
        return self.map[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)