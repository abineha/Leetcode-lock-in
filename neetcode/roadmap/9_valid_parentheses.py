class Solution:
    def isValid(self, s: str) -> bool:
        stak=[]
        for i in s:
            if i=="{" or i=="(" or i=="[":
                stak.append(i)
            elif i=="}":
                if stak==[]:
                    return False
                else:
                    if stak[-1]=="{":
                        stak.pop()
                    else:
                        return False
            elif i==")":
                if stak==[]:
                    return False
                else:
                    if stak[-1]=="(":
                        stak.pop()
                    else:
                        return False
            elif i=="]":
                if stak==[]:
                    return False
                else:
                    if stak[-1]=="[":
                        stak.pop()
                    else:
                        return False
        if stak==[]:
            return True
        else:
            return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid(s = "()"))