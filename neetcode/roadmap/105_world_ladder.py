from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        
        neigh = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):  # patterns
                pattern = word[:j] + "*" + word[j+1:]
                neigh[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        result = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return result
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighword in neigh[pattern]:
                        if neighword not in visit:
                            visit.add(neighword)
                            q.append(neighword)
            result += 1
            
        return 0