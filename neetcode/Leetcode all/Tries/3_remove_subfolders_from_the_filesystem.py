from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder_set = set(folder)
        result = []

        for f in folder:
            result.append(f)
            for i in range(len(f)):
                if f[i] == '/' and f[:i] in folder_set:
                    result.pop()
                    break

        return result
    
# TRIE

class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

    def add(self, path):
        cur = self
        
        for f in path.split('/'):
            if f not in cur.children:
                cur.children[f] = Trie()
            cur = cur.children[f]
        
        cur.end = True
    
    def prefix_search(self, path):
        cur = self
        folder = path.split('/')

        for i in range(len(folder)-1):
            cur = cur.children[folder[i]]
            if cur.end:
                return True
        
        return False
        
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()

        for f in folder:
            trie.add(f)
        
        result = []

        for f in folder:
            if not trie.prefix_search(f):
                result.append(f)
        
        return result