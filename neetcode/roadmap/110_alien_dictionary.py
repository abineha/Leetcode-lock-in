class Solution:
    def alienOrder(self, words: list[str]) -> str:
        adj = {c:set() for w in words for c in w} # adjacency list for each unique character in all words

        for i in range(len(words)-1):       # Builds the graph based on character order in adjacent words
            w1, w2 = words[i], words[i+1]
            minlen = min(len(w1), len(w2))
            if w1[:minlen] == w2[:minlen] and len(w1) > len(w2):    # Invalid case: word1 is longer and word2 is its prefix (e.g., "abc", "ab")
                return ""
        
            for j in range(minlen):     # # Compare characters of both words to find the first different character
                if w1[j] != w2[j]:      # This means w1[j] comes before w2[j] in alien language
                    adj[w1[j]].add(w2[j])   # w1 < w2
                    break               # only the first difference matters
            
        visit = {}      # F = visited, T = current path, True = visiting, False = visited
        result = []

        def dfs(c):
            if c in visit:
                return visit[c]     # True: cycle found, if False: already processed
            visit[c] = True     # visiting in current path

            for nei in adj[c]:
                if dfs(nei):    # loop detected
                    return True
            
            visit[c] = False    # mark as visited (no cycle from this node)
            result.append(c)    # add character to result after visiting all dependencies

        for c in adj:
            if dfs(c):  # loop detected
                return ""
        
        result.reverse()
        return "".join(result)