class Solution:
    def compress(self, chars: list[str]) -> int:
        i, j = 0, 0

        while j < len(chars):
            c = chars[j]
            count = 0

            while j < len(chars) and chars[j] == c:
                j += 1
                count += 1
            
            chars[i] = c
            i+= 1

            if count > 1:
                for d in str(count):
                    chars[i] = d
                    i += 1

        return i
        
      