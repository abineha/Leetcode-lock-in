class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        result = 0
        l, r = 0, len(people)-1

        while l <= r:
            remain = limit - people[r]  # put heaviest person on boat
            r -= 1
            result += 1     # allocate 1 boat
            if l <= r and people[l] <= remain:
                l += 1
            
        return result
    
# COUNTING SORT
class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        m = max(people)
        count = [0] * (m + 1)
        for p in people:
            count[p] += 1
        
        idx, i = 0, 1
        while idx < len(people):
            while count[i] == 0:
                i += 1
            people[idx] = i
            count[i] -= 1
            idx += 1

        res, l, r = 0, 0, len(people) - 1
        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remain >= people[l]:
                l += 1
        return res