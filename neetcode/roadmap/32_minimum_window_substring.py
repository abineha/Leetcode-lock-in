class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t =="":
            return ""
        
        count_t, window = {}, {}
        for char in t:
            count_t[char] = 1 + count_t.get(char, 0)

        have, need = 0, len(count_t)
        result, result_len = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = 1  + window.get(char, 0)

            if char in count_t and window[char] == count_t[char]:
                have +=1
            
            while have == need:
                if (r - l + 1) < result_len:
                    result = [l, r]
                    result_len = r - l + 1

                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l, r = result
        return s[l: r + 1] if result_len != float("infinity") else ""
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow(s = "ADOBECODEBANC", t = "ABC"))