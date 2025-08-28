from typing import List

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        dp = { len(s): 0 }

        def dfs(i):
            if i in dp:
                return dp[i]

            result = 1+dfs(i+1)

            for j in range(i, len(s)):
                if s[i:j+1] in words:
                    result = min(result, dfs(j+1))
            
            dp[i] = result 
            return result
        
        return dfs(0)
    
# TRIE

# Each node of the Trie
class TrieNode:
    def __init__(self):
        self.children = {}   # dictionary to store child nodes (key = character, value = TrieNode)
        self.word = False    # marks the end of a word (True if a word ends here)

# Trie data structure to store all words from the dictionary
class Trie:
    def __init__(self, words):
        self.root = TrieNode()  # root node of the Trie
        
        # Insert each word into the Trie
        for w in words:
            cur = self.root
            for c in w:  # traverse each character in the word
                if c not in cur.children:    # if character not present, create a new node
                    cur.children[c] = TrieNode()
                cur = cur.children[c]        # move to the child node
            cur.word = True   # mark end of the word

# Main solution class
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # dp[i] = minimum extra chars needed from index i to end of string
        dp = { len(s): 0 }  
        
        # Build Trie from dictionary
        trie = Trie(dictionary).root

        # Recursive DFS with memoization
        def dfs(i):
            # If result already computed, return it
            if i in dp:
                return dp[i]

            # Option 1: treat s[i] as extra char -> cost = 1 + dfs(i+1)
            result = 1 + dfs(i+1)
            
            cur = trie
            # Option 2: try to match dictionary words starting at index i
            for j in range(i, len(s)):
                if s[j] not in cur.children:  # if no path in Trie, stop searching
                    break
                cur = cur.children[s[j]]
                
                # If a word ends here, we can jump to next index after word
                if cur.word:
                    result = min(result, dfs(j+1))

            # Save result in dp table (memoization)
            dp[i] = result
            return result
        
        # Start DFS from index 0
        return dfs(0)
