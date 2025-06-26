class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        count = 0
        map = {}
        for s in emails:
            filter = ""
            for c in range(len(s)):
                if s[c] == "@":
                    filter += s[c:]
                    break
                if s[c] == ".":
                    continue
                if s[c] == "+":
                    for i in range(c,len(s)):
                        if s[i] == "@":
                            filter += s[i:]
                            break
                    break
                filter += s[c]
            map[filter] = map.get(filter, 0) + 1
            if map[filter] == 1:
                count +=1
        print(map)
        return count
        
class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        s = set()
        for i in emails:
            local, domain = i.split("@")
            local = local.replace(".", "")
            local = local.split("+")[0]
            s.add(local + "@" + domain)
        return len(s)