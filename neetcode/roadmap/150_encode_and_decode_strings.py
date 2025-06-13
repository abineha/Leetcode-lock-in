class Solution:
    def encode(self, strs):
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result
    
    def decode(self, strs):
        result, i = [], 0

        while i < len(strs):
            j = i
            while strs[j] != "#":
                j += 1
            length = int(strs[i:j])
            result.append(strs[j+1 : j+1+length])
            i = j + 1 + length

        return result

