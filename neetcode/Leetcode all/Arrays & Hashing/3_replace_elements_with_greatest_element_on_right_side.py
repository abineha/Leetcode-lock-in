class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        great = arr[-1]
        arr[-1] = -1
        for i in range(len(arr) - 2, -1,-1):
            temp = great
            great = max(great, arr[i])
            arr[i] = temp
        return arr