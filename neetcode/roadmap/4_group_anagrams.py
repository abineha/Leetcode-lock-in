from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d=defaultdict(list)
        for w in strs:
            count=[0]*26
            for c in w:
                count[ord(c)-ord('a')]+=1
            d[tuple(count)].append(w)
        return list(d.values())

if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))