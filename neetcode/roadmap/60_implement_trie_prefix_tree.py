class TrieNode:
    def __init__(self):
        self.children = {}  # hashmap for 26 letters of TrieNode type
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root  # start at root

        for c in word:  # char by char in word
            if c not in cur.children:  # not in hashmap
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root  # start at root

        for c in word:
            if c not in cur.children:  # not in hashmap
                return False
            cur = cur.children[c]

        return cur.end  # reached end of word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root  # start at root

        for c in prefix:
            if c not in cur.children:  # not in hashmap
                return False
            cur = cur.children[c]
            
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)