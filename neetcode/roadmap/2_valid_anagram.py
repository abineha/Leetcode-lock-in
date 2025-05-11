class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sd,td={},{}
        for i in range(len(s)):
            sd[s[i]]=sd.get(s[i],0)+1
            td[t[i]]=td.get(t[i],0)+1
        if sd==td:
            return True
        else:
            return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram(s="anagram",t="nagaram"))