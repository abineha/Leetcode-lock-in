class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        arr = list(zip(heights,names))
        arr.sort(reverse= True)
        return [names for _, names in arr]
        