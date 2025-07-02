class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        l = sentence.split(" ")
        for w in range(len(l) - 1):
            if l[w][-1] == l[w+1][0]:
                continue
            else:
                return False
        if l[0][0] == l[-1][-1]:
            return True
        else:
            return False
        
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        w = sentence.split(" ")

        for i in range(len(w)):
            if w[i][0] != w[i - 1][-1]:
                return False

        return True