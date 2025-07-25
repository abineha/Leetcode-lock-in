class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        index_s, index_t = len(s) - 1, len(t) - 1
        backspace_s = backspace_t = 0
        
        while True:
            while index_s >= 0 and (backspace_s or s[index_s] == '#'):
                backspace_s += 1 if s[index_s] == '#' else -1
                index_s -= 1

            while index_t >= 0 and (backspace_t or t[index_t] == '#'):
                backspace_t += 1 if t[index_t] == '#' else -1
                index_t -= 1

            if not (index_s >= 0 and index_t >= 0 and s[index_s] == t[index_t]):
                return index_s == index_t == -1
            index_s, index_t = index_s - 1, index_t - 1 