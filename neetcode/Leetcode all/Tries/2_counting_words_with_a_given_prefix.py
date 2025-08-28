from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        N = len(pref)
        result = 0

        for w in words:
            if w[:N] == pref:
                result += 1
        
        return result
    
# TRIE
    
class PrefixNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class PrefixTree:
    def __init__(self):
        self.root = PrefixNode()
    
    def add(self, w, max_len):
        cur = self.root
        for c in w[:max_len]:   # only insert up to prefix length
            if c not in cur.children:
                cur.children[c] = PrefixNode()
            cur = cur.children[c]
            cur.count += 1  # increase count at each prefix
    
    def count(self, pref):
        cur = self.root
        for c in pref:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        return cur.count

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        prefix_tree = PrefixTree()
        max_len = len(pref)

        for w in words:
            if len(w) >= max_len:
                prefix_tree.add(w, max_len)  # stop early
        
        return prefix_tree.count(pref)
