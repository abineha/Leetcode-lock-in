class TrieNode:
    def __init__(self):
        self.children = {} # hashmap for 26 letters : TrieNode()
        self.end = False

    def addWord(self, word):
        cur = self
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]  # move to that node branch
        cur.end = True

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()

        for w in words:
             root.addWord(w)

        R, C = len(board), len(board[0])
        result, path = set(), set() # avoid same ele into consideration

        def dfs(r, c , node, word):
            if (r < 0 or c < 0 or r >= R or c >= C or (r, c) in path or board[r][c] not in node.children):
                    return 
            
            path.add((r, c))  # creating paths
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.end:
                 result.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            path.remove((r, c))  # backtracking

        for r in range(R):
             for c in range(C):
                  dfs(r, c, root, "")

        return list(result)