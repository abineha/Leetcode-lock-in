class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        map = {}
        result = len(students)

        for i in students:
            map[i] = map.get(i, 0) + 1

        for s in sandwiches:
            if map.get(s, -1) > 0 :
                result -= 1
                map[s] -= 1
            else:
                return result

        return result        